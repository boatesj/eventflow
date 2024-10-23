## Manual Testing Results for EventFlow Website

### Navigation and Page Interactions

| Feature                | Expected Outcome                       | Testing Performed          | Result                   | Pass/Fail |
|------------------------|----------------------------------------|----------------------------|--------------------------|-----------|
| Home Link              | Navigates to home page                 | Clicked Home Link           | Home page loaded          | Pass      |
| New Event Link         | New event form displays                | Clicked New Event link      | New event form displayed  | Pass      |
| New Category Link      | New category form displays             | Clicked New Category link   | New category form displayed | Pass      |
| Admin Dashboard Link   | Admin dashboard page displays          | Clicked Admin Dashboard link| Admin dashboard displayed | Pass      |
| Event Detail Link      | Event detail page displays             | Clicked Event Detail link   | Event detail page displayed | Pass      |
| Header links           | Text underlines when links are hovered | Hovered over each header link| Text underlined           | Pass      |

### New Event Page

| Feature              | Expected Outcome                       | Testing Performed          | Result                   | Pass/Fail |
|----------------------|----------------------------------------|----------------------------|--------------------------|-----------|
| Event Title Input     | Accepts and displays user input         | Entered title in input field| Title displayed correctly | Pass      |
| Event Description Input| Accepts and displays user input        | Entered description in input field | Description displayed correctly | Pass |
| Event Date Input      | Accepts and validates date input        | Entered valid date in date field | Date validated and displayed correctly | Pass |
| Event Time Input      | Accepts and validates time input        | Entered valid time in time field | Time validated and displayed correctly | Pass |
| Location Input        | Accepts and displays location input     | Entered location in location field | Location displayed correctly | Pass |
| Category Dropdown     | Displays available categories           | Selected category from dropdown | Category displayed correctly | Pass |
| Featured Event Checkbox | Toggles event as featured             | Checked featured event checkbox | Event marked as featured | Pass |
| Image Upload          | Uploads event image                    | Uploaded image for the event | Image uploaded and displayed correctly | Pass |
| Submit Button         | Submits the form and displays success message | Clicked submit button | Form submitted, success message displayed | Pass |

### New Category Page

| Feature              | Expected Outcome                       | Testing Performed          | Result                   | Pass/Fail |
|----------------------|----------------------------------------|----------------------------|--------------------------|-----------|
| Category Name Input    | Accepts and displays category input   | Entered category name       | Category name displayed correctly | Pass |
| Submit Button          | Submits the form and displays success message | Clicked submit button | Form submitted, success message displayed | Pass |

### Event Detail Page

| Feature              | Expected Outcome                       | Testing Performed          | Result                   | Pass/Fail |
|----------------------|----------------------------------------|----------------------------|--------------------------|-----------|
| RSVP Button           | Allows user to RSVP to event           | Clicked RSVP button         | RSVP confirmed, success message displayed | Pass |
| Event Information     | Displays correct event details         | Viewed event details        | Event details displayed correctly | Pass |

### Admin Dashboard

| Feature              | Expected Outcome                       | Testing Performed          | Result                   | Pass/Fail |
|----------------------|----------------------------------------|----------------------------|--------------------------|-----------|
| Event Count          | Displays total number of events        | Viewed admin dashboard      | Total event count displayed correctly | Pass |
| RSVP Count           | Displays total number of RSVPs         | Viewed admin dashboard      | Total RSVP count displayed correctly | Pass |


## Heroku Deployment and Testing

### Deployment to Heroku

**EventFlow** was successfully deployed to Heroku following the steps outlined below:

1. **Prepare the Environment**:
   - The `requirements.txt` file was updated to include all necessary dependencies for deployment (e.g., `Flask`, `Flask-SQLAlchemy`, `psycopg2`, `Flask-Migrate`).
   - The `Procfile` was created with the command to start the Flask app: `web: gunicorn app:app`.

2. **Set up Heroku App**:
   - A new app was created on Heroku using the Heroku CLI:
     ```bash
     heroku create eventflow-app
     ```

3. **Set Environment Variables**:
   - Environment variables were configured, including the secret key and the PostgreSQL database URL:
     ```bash
     heroku config:set SECRET_KEY=your_secret_key
     heroku config:set SQLALCHEMY_DATABASE_URI=postgresql://<db_url>
     ```

4. **Push Code to Heroku**:
   - The local repository was pushed to Heroku:
     ```bash
     git push heroku main
     ```

5. **Run Database Migrations**:
   - Once the app was deployed, database migrations were applied to set up the database:
     ```bash
     heroku run flask db upgrade
     ```

6. **Deploy and Check Logs**:
   - After deployment, the logs were monitored to ensure the app was running successfully:
     ```bash
     heroku logs --tail
     ```

### Heroku Testing

Testing on Heroku included the following areas:

#### 1. **Functionality Testing**
   - **Routes**: All routes (home, new event, new category, event detail, and admin dashboard) were tested to ensure proper rendering and functionality in the Heroku environment.
   - **Form Submissions**: Forms for creating events, categories, and RSVPs were submitted successfully, with flash messages confirming actions.

#### 2. **Database Testing**
   - **PostgreSQL Integration**: The app was connected to a PostgreSQL database hosted by Heroku. Data such as events, categories, and RSVPs were stored and retrieved without issues.
   - **Database Migrations**: Flask-Migrate was used to perform migrations, ensuring the schema was correctly set up for categories, events, and RSVPs.
   - **Real-time Updates**: The admin dashboard correctly displayed real-time updates for the total number of events and RSVPs, reflecting the live data stored in the Heroku PostgreSQL database.

#### 3. **Image Upload Testing**
   - **Image Storage**: Images uploaded through the event creation form were successfully stored and linked to their respective events. The upload functionality worked as expected, even with Heroku's ephemeral file system.

#### 4. **Responsive Design Testing**
   - **Cross-Device Testing**: The site was accessed on desktop, tablet, and mobile devices while deployed on Heroku. MaterializeCSS ensured the layout remained responsive across all screen sizes.
   - **Cross-Browser Testing**: The app was tested on Chrome, Firefox, Safari, and Microsoft Edge. The user experience and functionality were consistent across all browsers.

#### 5. **Performance Testing**
   - **Google Lighthouse**: After deployment, the performance of the Heroku-hosted app was tested using Google Lighthouse, focusing on load times, accessibility, SEO, and adherence to best practices. The results showed high scores, indicating good performance on Heroku.

#### 6. **Error Handling and Debugging**
   - **Logs Monitoring**: Heroku logs were continuously monitored during testing to ensure no errors or crashes occurred. No major issues were found, and the app ran smoothly in the Heroku environment.

### Conclusion of Heroku Testing
The **EventFlow** app passed all deployment and functionality tests on Heroku, confirming that the platform is fully functional, responsive, and stable in the cloud environment. The deployment process, including database migrations and environment setup, was successfully completed, and the app is now live for both admin and user interaction.
