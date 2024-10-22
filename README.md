# EventFlow

**EventFlow** is a dynamic and fully-functional web application designed to streamline event management. It allows users to easily create, view, and RSVP to events, while providing admin users with tools to manage categories and event details. Built with Flask and PostgreSQL, the application focuses on delivering an intuitive user experience while adhering to best practices in web development.

## Rationale

### Overview of the Project

The **EventFlow** project aims to address the need for an efficient, user-friendly platform to manage events. This project provides a comprehensive event management system that is easy to use for both end-users and administrators. The application supports full CRUD (Create, Read, Update, Delete) operations and allows users to interact with events in a meaningful way, whether it’s RSVPing or browsing through categorized event listings.

**EventFlow** was developed using modern web technologies such as Flask, SQLAlchemy, PostgreSQL, and JavaScript to ensure the application is responsive, accessible, and secure. The design focuses on ease of navigation and user interaction, making it suitable for a wide variety of event types, from social gatherings to professional conferences.

### Inspiration and Purpose

The inspiration behind **EventFlow** stemmed from the growing need for digital solutions to manage both large and small-scale events. Whether it's community gatherings, business events, or personal functions, users will have a centralised platform to organize and manage event details, categories, and RSVPs effectively. By addressing these needs, **EventFlow** enhances user experience while also simplifying the administrative process.

### Project Background

Event management tools often lack specific features that cater to both event organizers and participants. While many solutions exist, they are often either too complex or too limited for everyday users. **EventFlow** bridges that gap by offering an accessible yet feature-rich system, allowing both organizers and attendees to interact seamlessly.

During development, several challenges were identified, including setting up seamless event category management, properly displaying RSVPs, and ensuring the interface was responsive across multiple devices. Overcoming these obstacles helped shape a robust, easy-to-navigate platform.

### Scope and Limitations of the Project

#### Scope

The scope of the **EventFlow** project includes:
- Creation and management of events by admins.
- Categorization of events for easier navigation by users.
- RSVP system for users to indicate attendance.
- Display of event details, including date, time, description, category and images.
- Admin dashboard for managing events and categories.

#### Limitations

Known limitations of **EventFlow**:
- **No user authentication**: Users can interact with events (RSVP, view details) but cannot manage their accounts or receive personalized event suggestions.
- **Event image handling**: While images can be uploaded and managed, there are limitations in editing or resizing images through the interface.
- **Real-time notifications**: The current version of **EventFlow** does not send email notifications but only real-time on-page confirmation updates to users upon RSVPs.

## Strategic Solution

**EventFlow** offers a strategic solution to the event management needs of small to medium-sized organisations. Key features include:

- **Event Creation and Editing**: Admin users can create and manage events through a simple form interface, specifying the event title, date, time, description, and category.
- **Categorised Event Listings**: Users can filter events by categories such as "Workshops," "Conferences," or "Social Gatherings."
- **RSVP System**: Participants can RSVP to events and track their attendance.
- **Admin Dashboard**: Admins can oversee event management, including editing and deleting events, through an intuitive dashboard.
- **Flash Messages**: Action confirmation messages provide instant feedback for users and admins (e.g., "Event created successfully").

## Key Benefits

**EventFlow** offers several advantages:
- **Intuitive User Interface**: The platform provides a clean and intuitive interface for managing events and RSVPs.
- **Admin Dashboard**: Admins can manage all aspects of event creation, including category assignment, event editing, and deletion.
- **Responsive Design**: The app is fully responsive, ensuring it works across desktop, tablet, and mobile devices.
- **Search Functionality**: Users can easily search for events by title or description, streamlining event discovery.

## Features

- **Full CRUD Operations**: Event creation, reading, updating, and deleting is fully supported.
- **Event Categorization**: Admins can add new event categories, which are displayed to users when they filter events.
- **RSVP Functionality**: Users can RSVP to events and update their attendance.
- **Flash Messages**: Confirmation messages are displayed for actions like adding or deleting events.
- **Admin Dashboard**: Admin users can manage categories and events from a dedicated interface.

## Technologies Used

- **HTML5**: For structuring content and building the front end.
- **CSS3**: Styling for a responsive and visually appealing design.
- **JavaScript (jQuery)**: Added interactivity for features like RSVP and form handling.
- **Flask (Python)**: Web framework to handle backend functionality.
- **PostgreSQL**: Relational database to manage event and RSVP data.
- **SQLAlchemy**: Object-relational mapping (ORM) for database queries.
- **Heroku**: Cloud platform for deployment.
- **Materializecss**: Framework for responsive design.

## Installation

### Local Installation

To run **EventFlow** locally:

1. Clone this repository:
 
   git clone https://github.com/yourusername/eventflowmax.git

2. Navigate to the directory:
   
   cd eventflow

3. Set up a virtual environment:
  
     python3 -m venv venv

4. Activate the virtual environment:

- **For Mac/Linux**:

     source venv/bin/activate

- **For Windows**:
  
     venv\Scripts\activate

5. Install required packages:

     pip install -r requirements.txt

6. Set up environment variables in an .env or env.py file:

     SECRET_KEY=your_secret_key
     SQLALCHEMY_DATABASE_URI=postgresql:///eventflow

7. Set up the database:

     flask db upgrade

8. Run the application:

     flask run


# Database Structure

The database for EventFlow consists of three main models:

## 1. Category Model
- **Fields:** 
  - `id`: Primary key
  - `category_name`: Unique category name (e.g., Conference, Workshop)
- **Description:** Handles different event categories, allowing events to be organized into various groups.

## 2. Event Model
- **Fields:** 
  - `id`: Primary key
  - `event_title`: Title of the event
  - `event_description`: Detailed description of the event
  - `event_date`: Date of the event
  - `event_time`: Time of the event
  - `category_id`: Foreign key linking to the Category model
- **Description:** Stores the event's details like title, description, date, and time, along with its category association.

## 3. RSVP Model
- **Fields:** 
  - `id`: Primary key
  - `event_id`: Foreign key linking to the Event model
  - `user_email`: Email of the user who RSVPs
- **Description:** Tracks RSVPs for events by storing the user’s email and associating it with the event they registered for.


# Deployment

## Deployment to Heroku

Follow these steps to deploy EventFlow to Heroku:

### 1. Install the Heroku CLI

Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) on your local machine.

### 2. Create a New Heroku App

Create a new Heroku app by running the following command in your terminal:

```bash
heroku create eventflow-app

### Set Environment Variables

Set the necessary environment variables for your Heroku app. Replace `your_secret_key` with your actual secret key and `<db_url>` with your PostgreSQL database URL:

```bash
heroku config:set SECRET_KEY=your_secret_key
heroku config:set SQLALCHEMY_DATABASE_URI=postgresql://<db_url>

### Push Your Code to Heroku

To deploy your local code to Heroku's remote repository, use the following command:

```bash
git push heroku main

### Run Database Migrations on Heroku


Once the code is deployed, run the following command to apply database migrations on Heroku:

```bash
heroku run flask db upgrade











