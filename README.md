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
- **Advanced Search**: Users can search events using filters for event categories, dates, and locations.

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
 
   git clone https://github.com/boatesj/eventflow

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

- **Desktop Wireframe**: ![View Desktop Wireframe](/eventflow/static/wireframes/eventflowmax-app.png)
<br><br>
- **Tablet Wireframe**: ![View Tablet Wireframe](/eventflow/static/wireframes/eventflowApp-tablet.png)
<br><br>
- **Mobile Wireframe**: ![View Mobile Wireframe](/eventflow/static/wireframes/EventflowApp-mob.png)

## Features

### 1. Adding a New Category
- Admins have the ability to add new event categories through a dedicated form. This feature allows the platform to accommodate various event types, ensuring that events are well-organized and easy to filter.
- After submitting the form, a flash confirmation message is displayed to confirm the successful creation of the category.
- The category list is immediately updated, making the new category available for event assignment.

### 2. Adding a New Event
Admins can create new events by filling out a detailed form. The event creation form includes the following fields:
- **Event Title**: The name of the event.
- **Event Description**: A detailed description of what the event is about.
- **Event Date**: The scheduled date of the event.
- **Event Time**: The specific time the event will take place.
- **Location**: The venue or address of the event.
- **Category Selection**: A dropdown menu that allows the admin to choose a category for the event.
- **Mark as Featured**: An option to highlight the event as featured, making it more prominent on the homepage.
- **Upload Event Image**: Allows admins to upload an image related to the event to enhance its presentation.

Once the event details are submitted, a flash confirmation message confirms that the event has been successfully added. The new event is immediately visible in the list of events and is displayed in its respective category.

### 3. Home Page
The homepage provides users with an overview of all available events, along with tools to help them find specific events:
- **Search Event**: Users can search for events using several filters:
  - **Category**: Filter events based on their assigned category.
  - **Start and End Date**: Select a range of dates to filter events happening within that period.
  - **Location**: Search events based on their location.
  - **Sort by Date or Popularity**: Users can sort events either by the date of occurrence or by their popularity (based on RSVPs).

- **Featured Events Section**: Highlights events that have been marked as "featured" by admins. These events are more prominently displayed to attract user attention.

- **Upcoming Events Section**: Displays events that are scheduled to happen in the near future, sorted by date.

- **Past Events**: Lists events that have already occurred, providing users with access to information about previous events.

### 4. Event Detail Page
Each event has a dedicated detail page that provides users with comprehensive information:
- **Event Description**: A full description of the event, including the date, time, and location.
- **RSVP Feature**: Users can confirm their attendance by clicking the RSVP button. Upon submitting an RSVP, the user receives a flash confirmation message to confirm their RSVP.
- **Edit Event**: For admins, the event detail page provides an option to edit the event’s details. Admins can update any of the event fields and re-upload images if necessary.
- **Delete Event**: Admins can also delete events directly from the detail page. A confirmation message ensures that events are only deleted with admin approval.

### 5. Admin Dashboard
The admin dashboard provides a comprehensive overview of the event management system:
- **Total Events**: Displays the total number of events currently in the system, giving admins a quick snapshot of how many events are active.
- **Total RSVPs**: Shows the total number of RSVPs across all events, allowing admins to gauge event popularity and attendee engagement.

The dashboard is designed to provide admins with quick access to important metrics, helping them manage the event system effectively.

## Website Structure and Content

### 1. Website Structure

**EventFlow** includes four main pages, along with dynamically generated event detail pages, to provide both users and admins with comprehensive event management tools:

- **Home Page**: 
  - The home page offers an overview of all events, with a search feature that allows users to filter events by category, date range, location, and popularity. 
  - It also features sections for featured events, upcoming events, and past events, giving users quick access to relevant event information.

- **New Event Page**: 
  - Admins can create new events through this page by filling out details such as event title, description, date, time, location, and category, with the option to upload an event image and mark the event as featured.
  - Flash confirmation messages confirm when an event has been successfully created.

- **New Category Page**: 
  - This page allows admins to create new event categories to help organize events. The form is straightforward and includes a flash confirmation message to notify admins when a new category has been added successfully.

- **Admin Dashboard**: 
  - The admin dashboard provides a quick summary of the total number of events and RSVPs in the system. 
  - It also offers links to manage existing events and categories, giving admins full control over the platform's content.

- **Dynamically Created Event Detail Pages**: 
  - Each event has its own dynamically generated detail page, displaying key information such as the event title, description, date, time, location, and category.
  - Users can RSVP directly from this page, with a flash confirmation message appearing upon successful RSVP submission.

### 2. Responsive Design

The **EventFlow** website is fully responsive, ensuring that all pages, including dynamically created event detail pages, display correctly on a range of devices:

- **MaterializeCSS** provides the foundation for the responsive design. The framework’s grid system and components adjust automatically based on screen size, ensuring optimal usability on desktops, tablets, and mobile devices.
- **Custom CSS media queries** are used to fine-tune the responsiveness, ensuring that text, images, and interactive elements are appropriately scaled across all screen sizes.

### 3. User Interaction

**EventFlow** includes several interactive features to enhance user and admin experiences:

- **Event Search and Filters**: 
  - Users can filter events by category, date range, and location, and sort events by date or popularity. 
  - Search results are updated dynamically, making it easy for users to find the events they are interested in.

- **RSVP Functionality**: 
  - On each dynamically created event detail page, users can RSVP to events with a single click. 
  - A flash message confirms successful RSVPs, providing real-time feedback to users.

- **Admin Functions**: 
  - Admins can create, edit, and delete events and categories. 
  - They also have access to a user-friendly dashboard that displays key metrics like the total number of events and RSVPs, streamlining event management.

- **Form Interaction**: 
  - All forms across the platform are easy to use, featuring input validation to ensure all required fields are completed before submission. 
  - Flash confirmation messages notify users and admins of successful actions, such as adding an event or category.

## Accessibility

**EventFlow** was designed with accessibility in mind, following WCAG 2.1 guidelines to ensure the platform is usable by a wide range of users, including those with disabilities.

### Key Accessibility Features

- **Text Alternatives for Non-Text Content**: 
  - The only images used on the platform are those uploaded by the admin to highlight events.
  - Each of these images includes appropriate alt text, describing the event or the purpose of the image, ensuring that users relying on screen readers can understand the context of the image.

- **Keyboard Accessibility**: 
  - All interactive elements, such as navigation links, buttons, and forms, are fully accessible via keyboard.
  - Users can navigate through the site and interact with all features, such as filtering events or submitting RSVPs, without the need for a mouse.

- **Sufficient Contrast Ratios**: 
  - The platform’s color scheme (using MaterializeCSS Lime Darken-4, Lime Darken-3, and Red Darken-4) was selected to ensure high contrast between text and background.
  - This makes content easily readable for users with visual impairments or color blindness.

### Additional Considerations

- **Semantic HTML**: 
  - The use of semantic HTML elements (e.g., header, nav, main, section, article) helps create a logical structure that is easy to navigate for screen readers and other assistive technologies.

- **ARIA Labels**: 
  - Where necessary, ARIA (Accessible Rich Internet Applications) labels are used to provide additional context to screen reader users, particularly for interactive elements like buttons and forms.

By focusing on these accessibility features, **EventFlow** provides an inclusive experience for all users while ensuring compliance with modern web accessibility standards. This approach enhances usability and lays the groundwork for future improvements in accessibility.


## Bugs Fixed in the EventFlow Website

During the development and ongoing maintenance of **EventFlow**, several key issues were identified and resolved to enhance the platform’s performance, usability, and functionality. Below is a list of significant bugs that were fixed, along with the solutions implemented.

### List of Bugs and Fixes

#### 1. Category Dropdown Not Displaying
- **Problem**: The category dropdown on the event creation page was not displaying available categories correctly.
- **Fix**: The database query in the form handler was adjusted to ensure categories are fetched and displayed correctly in the dropdown.

#### 2. Flash Confirmation Messages Not Displaying Properly
- **Problem**: Flash messages confirming actions like adding a new event or category were not appearing in the intended location on the page.
- **Fix**: The Flask route handlers were updated to ensure that flash messages are passed correctly to the templates, and the HTML structure was modified to display the messages in the appropriate section.

#### 3. Image Upload Errors
- **Problem**: Admins encountered issues when uploading images for events, particularly when the file size exceeded certain limits.
- **Fix**: Image upload functionality was optimized by setting file size limits and ensuring proper error handling when large files were uploaded. Additionally, the upload path was checked to ensure images are correctly stored and linked to the events.

#### 4. RSVP Button Not Functioning Correctly on Event Detail Page
- **Problem**: The RSVP button was not submitting responses or reflecting user confirmation on the event detail page.
- **Fix**: JavaScript and form validation scripts were reviewed and corrected to ensure that the RSVP functionality works as intended, with proper feedback provided via flash messages after successful submissions.

#### 5. Admin Dashboard Not Updating Event and RSVP Counts
- **Problem**: The admin dashboard was not showing real-time updates for the total number of events and RSVPs.
- **Fix**: The database queries on the admin dashboard were updated to ensure accurate counts of total events and RSVPs, allowing for real-time tracking of metrics.

## Testing

### Automated Testing

- **W3C Markup Validator**: All HTML pages in **EventFlow** were validated using the W3C Markup Validator to ensure there were no syntax errors and that the code followed web standards. Each page passed the validation process without issues. [Check HTML Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Feventflowmax-3d21a4c0c847.herokuapp.com%2F)

- **W3C CSS Validator**: The custom CSS and MaterializeCSS were validated using the W3C CSS Validator. While the custom CSS passed validation without any errors, an issue was found in the MaterializeCSS library. Specifically, a minor validation error related to the letter-spacing property in MaterializeCSS was flagged, indicating that a unit was missing for the value 0.4. Since this issue is part of the external library and does not impact the functionality or responsiveness of the website, I decided to leave it unchanged. Despite this external issue, the custom CSS was confirmed to be fully compliant with web standards, ensuring that the website's layout remains responsive and functions correctly across all devices. [Check CSS Validation](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Feventflowmax-3d21a4c0c847.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

- **JavaScript Linting**: Custom JavaScript, including code for event filtering, RSVP submissions, and dynamic form handling, was tested using linting tools to ensure it adhered to best practices and contained no errors. [Check JSHint Validation](/eventflow/static/wireframes/JSHint-ef.png)

- **Python (PEP8) Validation**: The Python code used in **EventFlow**, including Flask routes, models, and other logic, was validated using PEP8 standards. Tools like flake8 and pylint were used to ensure that the code is clean, readable, and follows Python's style guidelines.

- **Flask Testing Suite**: Python’s built-in unittest framework was used to create automated tests for Flask routes and back-end logic. The test cases ensured that routes for creating events, RSVPs, and category management were functioning correctly and that server responses were accurate.

- **Lighthouse Testing**: Google Lighthouse was used to test the performance, accessibility, SEO, and best practices of the website. The results were excellent, showing good performance scores and accessibility compliance with web standards. [Check Lighthouse testing](https://lighthouse-metrics.com/lighthouse/checks/ca7e3ae7-22bd-4b67-93bb-019ce217faf5)

### Manual Testing

For detailed manual testing information, please refer to the [testing documentation](./testing.md). Below is a summary of the main manual tests conducted:

#### Testing User Stories from User Experience (UX) Section

**First Time Visitor Goals**:
- *Goal*: Easily understand the purpose of the site and learn more about events.
  - *Result*: The homepage clearly presents **EventFlow**'s purpose, showcasing featured and upcoming events, and providing easy access to event information.
  
- *Goal*: Easily navigate the site.
  - *Result*: Users can navigate the platform, filter events by category, date, and location, and view event details across devices.

**Returning Visitor Goals**:
- *Goal*: Find detailed information about upcoming events.
  - *Result*: The event detail pages provide comprehensive information, including the event's title, description, location, and RSVP options.
  
- *Goal*: RSVP to events and confirm attendance.
  - *Result*: The RSVP feature works smoothly, providing users with feedback through flash messages and updating the admin dashboard.

**Admin User Goals**:
- *Goal*: Create, edit, and delete events and categories.
  - *Result*: Admin functionalities were tested extensively to ensure event creation, editing, deletion, and category management features work as expected. Flash confirmation messages provide feedback after each action.
  
- *Goal*: See an overview of total events and RSVPs.
  - *Result*: The admin dashboard accurately displays the number of active events and RSVPs, providing a quick snapshot of platform activity.

### Python Code Testing

- **PEP8 Compliance**: All Python code (routes, models, and utilities) was checked against PEP8 standards using tools like flake8 to ensure that it follows best practices in Python development.
  
- **Unit Testing**: Unit tests were created for Flask routes and back-end logic using Python's unittest module. The tests ensured:
  - Routes respond with the correct status codes and templates.
  - Database interactions with models for event and RSVP management are correct.
  - Flash messages display appropriately after actions like adding or editing events.
  - Form validation works as expected with proper error handling for invalid inputs.

- **Manual Code Review**: The Python codebase was manually reviewed to ensure that logic flow, error handling, and database interactions were correct, avoiding issues like duplicate entries or incorrect data retrieval.

### Further Testing

- **Cross-Browser Testing**: **EventFlow** was tested across multiple browsers (Chrome, Firefox, Safari, and Microsoft Edge) to ensure consistent behavior and compatibility.

- **Responsive Testing**: The site was tested on various devices (desktops, tablets, smartphones) to verify that it remains responsive and user-friendly across all screen sizes.

- **Form Validation**: All forms (event creation, category creation, RSVP submissions) were manually tested to ensure data was captured and processed correctly. Invalid submissions were handled with appropriate error messages.

### Known Bugs

There are no known bugs in the current version of **EventFlow**. All issues identified during testing were resolved prior to deployment.



## Acknowledgements

- **Font Awesome**: For providing the icons used throughout the site, enhancing visual clarity and improving the user experience.
- **MaterializeCSS**: For offering a responsive framework that made the front-end development process faster and more efficient, ensuring consistent design across all devices.
- **Flask Documentation**: For providing guidance and best practices throughout the development of the back-end functionality.
- **Stack Overflow & Code Institute**: For the community-driven solutions and educational resources that assisted in solving development challenges.
- **Heroku**: For hosting the **EventFlow** app and enabling the deployment of images stored in the local project directory.
















