import sys
import os
from flask import request, redirect, url_for, flash, render_template, jsonify
from werkzeug.utils import secure_filename
from eventflow import app, db
from eventflow.models import Event, Category, RSVP
from datetime import datetime, timedelta
from flask_login import current_user
import json

# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Combine separate date and time fields into a datetime object
def combine_date_and_time(event):
    if event.event_date and event.event_time:  # Updated to event_date and event_time
        return datetime.combine(event.event_date, event.event_time)
    return None

# Home page showing list of all upcoming and past events
@app.route("/")
def home():
    sort_by = request.args.get("sort_by", "date")
    order = request.args.get("order", "asc")

    now = datetime.now().date()  # Use only the date part of the current datetime
    featured_events = Event.query.filter_by(featured=True).all()

    # Sort events by the combined datetime
    featured_events.sort(key=combine_date_and_time, reverse=(order == "desc"))

    if sort_by == "date":
        if order == "asc":
            upcoming_events = Event.query.filter(Event.event_date >= now).all()
            past_events = Event.query.filter(Event.event_date < now).all()  # Corrected to event_date
        else:
            upcoming_events = Event.query.filter(Event.event_date >= now).all()  # Corrected to event_date
            past_events = Event.query.filter(Event.event_date < now).all()  # Corrected to event_date

        # Sort the events by combined date and time
        upcoming_events.sort(key=combine_date_and_time, reverse=(order == "desc"))
        past_events.sort(key=combine_date_and_time, reverse=(order == "desc"))

    return render_template("events.html", upcoming_events=upcoming_events, past_events=past_events, featured_events=featured_events, user=current_user)

# Add event details
@app.route("/event/<int:event_id>", methods=["GET", "POST"])
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    rsvps = RSVP.query.filter_by(event_id=event_id).all()

    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")
            attending = request.form.get("attending") == "1" if request.form.get("attending") else False

            existing_rsvp = RSVP.query.filter_by(event_id=event_id, email=email).first()

            if existing_rsvp:
                existing_rsvp.attending = attending
                existing_rsvp.name = name
                db.session.commit()
                flash(f"RSVP updated successfully for {email}!", "success")
            else:
                rsvp_entry = RSVP(event_id=event_id, name=name, email=email, attending=attending)
                db.session.add(rsvp_entry)
                db.session.commit()
                flash(f"RSVP submitted successfully for {email}!", "success")

            return redirect(url_for("event_detail", event_id=event_id))

        except Exception as e:
            db.session.rollback()
            flash(f"Error submitting RSVP: {str(e)}", "error")
            return redirect(url_for("event_detail", event_id=event_id))

    return render_template("event_detail.html", event=event, rsvps=rsvps)

# Create a new event
@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    categories = Category.query.all()
    if request.method == "POST":
        try:
            event_title = request.form.get("event_title")
            description = request.form.get("description")
            event_date_raw = request.form.get("date")
            event_time_raw = request.form.get("time")
            location = request.form.get("location")
            category_id = request.form.get("category_id")
            featured = request.form.get("featured") == "1"

            day, month, year = map(int, event_date_raw.split('-'))
            hour, minute = map(int, event_time_raw.split(':'))
            event_date = datetime(year, month, day, hour, minute)

            file = request.files.get('image')
            filename = None
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.static_folder, 'images', filename)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                file.save(file_path)

            event = Event(
                event_title=event_title,
                event_description=description,
                event_date=event_date.date(),
                event_time=event_date.time(),
                location=location,
                category_id=category_id,
                featured=featured,
                image_file=filename
            )

            db.session.add(event)
            db.session.commit()
            flash('Event added successfully!', 'success')
            return redirect(url_for('home'))

        except Exception as e:
            db.session.rollback()
            flash(f'Error adding event: {str(e)}', 'error')
            return redirect(url_for('add_event'))

    return render_template("add_event.html", categories=categories)

# Edit an existing event
@app.route("/edit_event/<int:event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    categories = Category.query.all()

    if request.method == "POST":
        try:
            event_date_raw = request.form.get("date")
            event_time_raw = request.form.get("time")

            day, month, year = map(int, event_date_raw.split('-'))
            hour, minute = map(int, event_time_raw.split(':'))
            event.event_date = datetime(year, month, day).date()  # Updated to event_date
            event.event_time = datetime(year, month, day, hour, minute).time()  # Updated to event_time

            event.event_title = request.form.get("event_title")
            event.event_description = request.form.get("description")
            event.location = request.form.get("location")
            event.category_id = request.form.get("category_id")
            event.featured = request.form.get("featured") == "1"

            file = request.files.get('image')
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.static_folder, 'images', filename)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                file.save(file_path)
                event.image_file = filename

            db.session.commit()
            flash('Event updated successfully!', 'success')
            return redirect(url_for("home"))

        except Exception as e:
            db.session.rollback()
            flash(f"Error updating event: {str(e)}", 'error')
            return redirect(url_for("edit_event", event_id=event_id))

    formatted_date = event.event_date.strftime('%d-%m-%Y')  # Updated to event_date
    formatted_time = event.event_time.strftime('%H:%M')  # Updated to event_time
    return render_template("edit_event.html", event=event, categories=categories, formatted_date=formatted_date, formatted_time=formatted_time)

# Delete an event
@app.route("/delete_event/<int:event_id>")
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    RSVP.query.filter_by(event_id=event_id).delete()
    db.session.delete(event)
    db.session.commit()

    events = Event.query.order_by(Event.event_date.desc()).all()  # Updated to event_date
    rsvp_counts = {event.id: RSVP.query.filter_by(event_id=event.id).count() for event in events}
    total_events = len(events)
    total_rsvps = sum(rsvp_counts.values())

    return render_template("admin_dashboard.html", events=events, rsvp_counts=rsvp_counts, total_events=total_events, total_rsvps=total_rsvps)

# Create a new category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    categories = Category.query.all()

    if request.method == "POST":
        category_name = request.form.get("name").strip()
        existing_category = Category.query.filter_by(category_name=category_name).first()

        if existing_category:
            flash(f'Category "{category_name}" already exists.', 'error')
        else:
            if category_name:
                new_category = Category(category_name=category_name)
                db.session.add(new_category)
                db.session.commit()
                flash(f'Category "{category_name}" added successfully!', 'success')

        # After adding or encountering an error, stay on the same page
        return redirect(url_for("add_category"))

    return render_template("add_category.html", categories=categories)


# Search for events
@app.route("/search", methods=["GET", "POST"])
def search():
    categories = Category.query.all()

    if request.method == "POST":
        search_term = request.form.get("search_term", "").strip()
        search_query = f"%{search_term}%"

        selected_category = request.form.get("category_id")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        location = request.form.get("location", "").strip()
        sort_by = request.form.get("sort_by")

        query = Event.query.filter(
            (Event.event_title.ilike(search_query)) |
            (Event.event_description.ilike(search_query))
        )

        if selected_category:
            query = query.filter(Event.category_id == selected_category)

        if location:
            query = query.filter(Event.location.ilike(f"%{location}%"))

        if start_date:
            query = query.filter(Event.event_date >= datetime.strptime(start_date, '%Y-%m-%d').date())  # Updated to event_date
        if end_date:
            query = query.filter(Event.event_date <= datetime.strptime(end_date, '%Y-%m-%d').date())  # Updated to event_date

        if sort_by == "date":
            query = query.order_by(Event.event_date.asc())  # Updated to event_date
        elif sort_by == "popularity":
            query = query.outerjoin(RSVP).group_by(Event.id).order_by(db.func.count(RSVP.id).desc())

        matched_events = query.all()

        now = datetime.now().date()  # Use only the date part of the current datetime
        upcoming_events = [event for event in matched_events if event.event_date >= now]
        past_events = [event for event in matched_events if event.event_date < now]

        return render_template(
            "events.html",
            upcoming_events=upcoming_events,
            past_events=past_events,
            categories=categories,
            search_term=search_term,
            selected_category=selected_category,
            start_date=start_date,
            end_date=end_date,
            location=location,
            sort_by=sort_by
        )

    return redirect(url_for("home"))


@app.route("/admin_dashboard")
def admin_dashboard():
    events = Event.query.order_by(Event.event_date.desc()).all()
    rsvp_counts = {event.id: RSVP.query.filter_by(event_id=event.id).count() for event in events}
    total_events = len(events)
    total_rsvps = sum(rsvp_counts.values())

    return render_template("admin_dashboard.html", events=events, rsvp_counts=rsvp_counts, total_events=total_events, total_rsvps=total_rsvps)


# RSVP route
@app.route("/rsvp/<int:event_id>", methods=["POST"])
def rsvp(event_id):
    event = Event.query.get_or_404(event_id)

    name = request.form.get("name")
    email = request.form.get("email")

    if not name or not email:
        flash("Name and Email are required fields.", "error")
        return redirect(url_for('event_detail', event_id=event.id))

    attending = request.form.get("attending") is not None

    rsvp_entry = RSVP.query.filter_by(event_id=event.id, email=email).first()

    if rsvp_entry:
        rsvp_entry.attending = attending
        rsvp_entry.name = name
    else:
        rsvp_entry = RSVP(event_id=event.id, name=name, email=email, attending=attending)
        db.session.add(rsvp_entry)

    try:
        db.session.commit()
        flash('RSVP submitted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f"An error occurred while saving your RSVP: {str(e)}", 'error')

    return redirect(url_for('event_detail', event_id=event.id))
