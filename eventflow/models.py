from eventflow import db


class Category(db.Model):
    #schema for the category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), unique=True, nullable=False)
    events = db.relationship("Event", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        #__repr__to represent itself  in the form of a string
        return self.category_name


class Event(db.Model):
    # Schema for the event model
    id = db.Column(db.Integer, primary_key=True)
    event_title = db.Column(db.String(100), unique=True, nullable=False)
    event_description = db.Column(db.Text, nullable=False)
    event_date = db.Column(db.Date, nullable=False)  # Store only the date
    event_time = db.Column(db.Time, nullable=False)  # Store only the time
    location = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    featured = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    image_file = db.Column(db.String(120), nullable=True)


    # RSVP relationship
    rsvps = db.relationship('RSVP', backref='event', cascade="all, delete", lazy=True)

    
    def __repr__(self):
        return "#{0} - Event: {1} | Date: {2} | Time: {3} | Featured: {4}".format(
            self.id, self.event_title, self.event_date, self.event_time, self.featured
        )


class RSVP(db.Model):
    # Schema for the RSVP model
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id", ondelete="CASCADE"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    attending = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<RSVP {self.name} for Event {self.event.event_title}>"