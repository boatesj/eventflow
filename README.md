# EventFlow

**EventFlow** is a dynamic and fully-functional web application designed to streamline event management. It allows users to easily create, view, and RSVP to events, while providing admin users with tools to manage categories and event details. Built with Flask and PostgreSQL, the application focuses on delivering an intuitive user experience while adhering to best practices in web development.

![EventFlow Mockups](/eventflow/static/wireframes/eventflow-mockups.png)

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

```
## Testing

### Automated Testing
- **W3C HTML Validator**: Used to validate HTML files.
- **Flask Testing Suite**: Python's built-in `unittest` framework was used for unit testing.

### Manual Testing
- Cross-browser testing on Google Chrome, Firefox, and Safari.
- Tested responsiveness on multiple devices, including iPhones, Android phones, and tablets.
- Verified functionality by adding, editing, and deleting events, RSVPing, and managing categories.

## Future Enhancements
- **User Authentication**: Implement login functionality for users to manage their own events.
- **Calendar Integration**: Sync with Google Calendar for better event scheduling.
- **Email Notifications**: Automatically notify users of upcoming events they RSVP’d for.
- **Advanced Search**: Add filters for event categories, dates, and locations.

## Credits
- **Flask Documentation**: For backend functionality.
- **PostgreSQL Documentation**: For database management and queries.
- **Unsplash**: For placeholder images used in the app.
- **Bootstrap 5**: For responsive design components.

## License
This project is licensed under the MIT License.

## Conclusion

The **EventFlow** application is an innovative digital platform designed to manage events and enhance user engagement. By addressing the need for efficient, user-friendly solutions in event management, the application stands out with its comprehensive features, intuitive design, and focus on usability. 

The project not only offers immediate benefits to users and administrators but also holds potential for future enhancements that will keep it relevant and valuable in the long term.

By incorporating modern web technologies and focusing on user-centric design, **EventFlow** aims to simplify event management, making it more accessible, efficient, and engaging for everyone.


# Development Process

The development of **EventFlow** involved several key stages to ensure that both event organizers (admins) and participants (users) could manage and engage with events efficiently. Below is a detailed explanation of each stage:

### 1. Project Planning and Rationale

The rationale for **EventFlow** stems from the need for a streamlined event management platform that addresses challenges like scheduling, RSVPs, and communication between event organizers and attendees. Traditional methods, such as manual tracking or using disparate platforms, often lead to inefficiencies and a poor user experience. 

**EventFlow** consolidates these functionalities into a single platform where:
- **Admins** can easily manage events and categories.
- **Users** can quickly browse, RSVP, and stay informed about upcoming events.

This project aims to provide a solution that simplifies the overall event management process for organizers and enhances user engagement through a user-friendly interface. The integration of key features like event categorization and RSVP tracking ensures that both admins and users benefit from a cohesive and efficient system.


## Front-End and Back-End Technologies

**EventFlow** was developed using a combination of front-end and back-end technologies to deliver a fully functional, responsive, and interactive event management platform.

### Front-End Technologies

- **HTML**: The structure and content of the application are generated using Flask’s Jinja2 templating engine, which renders dynamic HTML for each page. All HTML files were validated using the W3C HTML Validator to ensure adherence to web standards.

- **CSS & MaterializeCSS**: MaterializeCSS was used to provide a modern, responsive design. Its built-in grid system, components (like modals, buttons, and forms), and media queries ensure that the application works seamlessly across desktops, tablets, and mobile devices. Additional custom CSS was used for unique design elements. CSS validation was performed using the W3C Jigsaw Validator.

- **JavaScript**: Interactivity on the client side was handled primarily through MaterializeCSS's JavaScript components (e.g., modals, dropdowns, and form validations). Additional custom JavaScript was used for handling specific tasks like RSVP submissions and event category filtering. These scripts were tested for functionality and compatibility across various browsers.

### Back-End Technologies

- **Flask**: Flask, a Python micro-framework, was used to manage the back-end logic, including routing, form handling, and request processing. Flask’s flexibility allowed for easy integration of the front-end and back-end, enabling dynamic content rendering and form validation.

- **Flask-SQLAlchemy**: The application uses Flask-SQLAlchemy, an Object-Relational Mapping (ORM) library, for managing interactions between Python objects and the database. This ensures seamless communication with the database, including creating, reading, updating, and deleting event and RSVP data.

- **PostgreSQL**: For database management, PostgreSQL was used. It is a powerful and scalable relational database that stores event details, categories, and RSVP data. PostgreSQL ensures that data is stored securely and is easily retrievable for both users and admins.

- **Flask-Migrate**: To handle database migrations and schema changes, Flask-Migrate was used. It integrates with SQLAlchemy and allows the project to maintain database consistency as new features or updates are implemented.

- **Jinja2**: Flask’s templating engine, Jinja2, was used to dynamically generate HTML pages. Jinja2 enables the rendering of Python variables, loops, and conditional statements within the HTML templates, ensuring a seamless connection between the front-end and back-end.


## User Experience (UX)

### User Stories

#### Admin Goals

1. **As an Admin, I want to create and manage events easily through a simple interface.**
   - Admins have access to an intuitive dashboard where they can add, edit, and delete events, categories, and view RSVP lists.
   - The admin dashboard simplifies the management of event details, allowing for quick updates and changes.

2. **As an Admin, I want to categorize events so users can find relevant events more easily.**
   - The event categorization feature allows admins to create, manage, and assign categories to events, making it easier for users to filter and browse events.

3. **As an Admin, I want to manage RSVPs efficiently to track event participation.**
   - The RSVP management system lets admins view who has RSVP’d to an event, helping them track expected attendance and prepare accordingly.

#### User Goals

1. **As a User, I want to easily browse and search for events relevant to my interests.**
   - Users are presented with a list of upcoming events, which can be filtered by categories like workshops, conferences, and social gatherings, allowing them to quickly find events that suit their interests.

2. **As a User, I want to quickly RSVP to events I am interested in attending.**
   - Users can RSVP to events directly from the event detail page or homepage, making the process of confirming attendance simple and straightforward.

3. **As a User, I want to view detailed information about events, including time, date, and description.**
   - Each event has its own dedicated page displaying all the necessary details, including the event description, date, time, and category, helping users make informed decisions about attending.

4. **As a User, I want to receive confirmation when I successfully RSVP to an event.**
   - After submitting an RSVP, users receive a confirmation message, ensuring they know their attendance has been registered.


## Design Choices

### Admin Design Considerations

- **Dashboard Navigation**: 
  - The admin dashboard is designed to be straightforward and intuitive, ensuring that administrators can easily manage events, categories, and RSVPs.
  - The dashboard provides clear, accessible links to all management functions, allowing admins to view, edit, and delete event information without unnecessary complexity.

- **Event Management**: 
  - The forms for creating and editing events are simple and user-friendly, enabling admins to quickly input or modify event details such as titles, descriptions, dates, and categories.
  - The layout ensures that event creation and updates can be done efficiently, streamlining the overall event management process.

### User Design Considerations

- **Navigation**: 
  - Users can easily browse through upcoming events and filter them by category, thanks to a clean and accessible navigation system.
  - A fixed top navigation bar provides consistent access to important sections like event listings and categories, ensuring a smooth user experience as they navigate through the site.

- **Responsive Design**: 
  - The platform is fully responsive, allowing both admins and users to access it from any device, including desktops, tablets, and mobile phones.
  - The responsiveness is achieved using MaterializeCSS, which ensures that the layout adapts seamlessly to different screen sizes without losing functionality or readability.

### Colour Scheme

The **EventFlow** colour scheme was chosen to maintain simplicity while emphasizing important actions and sections:

- **MaterializeCSS Lime Darken-4 (#827717)**: 
  - This colour is primarily used for the navigation bar and other key elements to provide a stable, professional backdrop for the site’s content.

- **MaterializeCSS Lime Darken-3 (#9E9D24)**: 
  - This lighter shade is used for accenting elements such as buttons and section headers, helping to create a sense of hierarchy and visual separation between different parts of the interface.

- **MaterializeCSS Red Darken-4 (#B71C1C)**: 
  - Red is used sparingly, primarily for critical actions like RSVP submissions or deletions. This colour draws attention to actions requiring user interaction or confirmation, helping to make the interface more intuitive.

By utilizing this limited colour palette, **EventFlow** maintains a clean and consistent visual style that enhances readability and user experience, while still providing enough contrast to highlight interactive elements.

## Font Awesome Icons

**Font Awesome** icons were used throughout the application to enhance the visual appeal and functionality of the user interface. Icons are used for various actions, such as:

- **Editing**: A pencil icon represents the edit functionality, making it clear that users can modify event details.
- **Deleting**: A trash icon is used to signify the delete function, providing a recognizable visual cue for removing events or RSVPs.
- **Submitting RSVPs**: An envelope or checkmark icon indicates the action to submit an RSVP, helping users easily identify the registration process.
- **Navigation Elements**: Icons such as arrows or home symbols are used to guide users through the application seamlessly.

The clean and recognizable icons provided by **Font Awesome** help users quickly understand the functionality of each button or link, improving the overall user experience.

## Wireframes

Wireframes were created to outline the structure and layout of the **EventFlow** website, ensuring a consistent and user-friendly design across devices.

- **Desktop Wireframe**: [View Desktop Wireframe](/eventflow/static/wireframes/eventflowmax-app.png)
- **Tablet Wireframe**: [View Tablet Wireframe](/eventflow/static/wireframes/eventflowApp-tablet.png)
- **Mobile Wireframe**: [View Mobile Wireframe](/eventflow/static/wireframes/EventflowApp-mob.png)













