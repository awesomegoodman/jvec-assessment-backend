# Contact Manager App

**Overview**

This project is a simple Contact Manager App with a backend RESTful API and a mobile frontend. It allows users to manage their contacts, including adding, updating, and deleting them. The backend is built using Django, while the mobile frontend is created with React Native.

**Features**

- User Registration and Authentication
- Create, Update, and Delete Contacts
- List and View Contact Details

**Installation**

**Backend:**

1. Ensure you have Python and Django installed.
2. Clone this repository.
3. Install required Python packages using `pip install -r requirements.txt`.
4. Apply database migrations with `python manage.py migrate`.
5. Start the Django server: `python manage.py runserver`.

**Mobile Frontend:**

1. Install Node.js and npm.
2. Clone the `jvec-assessment-mobile` repository.
3. Navigate to the project folder.
4. Install dependencies with `npm install`.
5. Run the app with `npx react-native run-android` (ensure an Android emulator or device is connected).

**API Endpoints**

- User Registration: `/users/create/`
- User Login: `/users/login/`
- User Logout: `/users/logout/`
- Create Contact: `/contacts/create/`
- List Contacts: `/contacts/list/`
- View Contact Details: `/contacts/detail/<contact_id>/`
- Update Contact: `/contacts/update/<contact_id>/`
- Delete Contact: `/contacts/delete/<contact_id>/`

**Authentication**

- Token-based authentication is used. Include the token in the header for authenticated requests.

**Unit Tests**

Unit tests are provided to ensure the functionality of the API. Run tests with `python manage.py test`.

**Security**

- Passwords are securely hashed.
- Rate limiting is in place to protect against brute-force attacks.
- Ensure your API is served over HTTPS.
- Validate and sanitize input data.
- Implement authentication and authorization for user actions.

**Error Handling**

Detailed error handling is implemented to provide informative responses.

**CORS**

Ensure that CORS policies are set up for your frontend's domain.

**Logging**

Set up logging to monitor and track unauthorized access.
