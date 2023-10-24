# Contact Manager Backend

## Overview

This project serves as the backend for a Contact Manager application, offering essential features for user management and contact operations. Users can seamlessly manage their contacts, including creation, updates, and removal.

## Key Features

- **User Management and Authentication**: Securely create, log in, and log out users.
- **Contact Operations**: Facilitate Create, Read, Update, and Delete (CRUD) actions on contacts.
- **Data Validation**: Ensure the accuracy of contact data through validation.
- **Database**: Employ PostgreSQL to securely store user and contact data.
- **Security**: Enhance security with token-based authentication and password hashing.
- **Unit Testing**: Maintain code reliability with unit tests for Create and Update API endpoints.

## Getting Started

1. Ensure you have Python and Django installed.
2. Clone this [repository](https://github.com/awesomegoodman/jvec-assessment-backend)
3. Install required Python packages: `pip install -r requirements.txt`.
4. Apply database migrations: `python manage.py migrate`.
5. Launch the Django server: `python manage.py runserver`.

## API Endpoints

- `POST /users/create`: Register a new user.
- `POST /users/login`: Log in to obtain an authentication token.
- `POST /users/logout`: Log out by invalidating the authentication token.
- `POST /contacts/create`: Add a new contact.
- `GET /contacts/list`: Retrieve a list of all contacts.
- `GET /contacts/detail/{contact_id}`: Retrieve details of a single contact.
- `PUT /contacts/update/{contact_id}`: Update a contact.
- `DELETE /contacts/delete/{contact_id}`: Delete a contact.

## Data Validation

- The API enforces data validation to guarantee well-formatted contact information.

## Database

- PostgreSQL serves as the database, ensuring secure storage of user and contact data.

## Security

- Token-based authentication ensures data security.
- Passwords are securely hashed.

## Unit Testing

- Unit tests have been implemented for the Create and Update API endpoints to validate code reliability.
- Run tests with `python manage.py test`.
