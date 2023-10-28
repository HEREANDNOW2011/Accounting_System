# Accounting_System

Flask Accounting System with User Authentication

This Flask application allows you to manage an accounting system where users can log in to add, view, and manage accounting entries. User authentication is implemented, and user credentials are stored in a credentials.txt file.
Features

    User authentication: Users must log in to access the accounting system.
    Secure user credentials: User credentials are stored in the credentials.txt file.
    Accounting system: Users can add, view, and manage accounting entries.
    CSV data storage: Accounting entries are stored in a CSV file (accounting_system.csv).

Prerequisites

Before running the application, ensure you have the following dependencies installed:

    Python 3
    Flask
    Flask-Login
    pandas (for CSV data manipulation)
    A code editor or IDE

Getting Started

    Clone this repository or download the source code to your local machine.

    Install the required dependencies using pip:

    bash

pip install Flask flask-login pandas

Customize the application:

    Modify credentials.txt: Add user credentials in the format username,password.
    Customize the application's routes, templates, and CSS to fit your needs.

Run the application:

bash

    python your_app_file.py

    Replace your_app_file.py with the name of your application file.

    Access the application in your web browser at http://localhost:5000.

Usage

    Visit http://localhost:5000/login to log in using your credentials.
    Once logged in, you can access the accounting system to add, view, and manage entries.
    Logout by clicking the "Logout" button.

Notes

    For a production environment, ensure user credentials are securely stored and hashed.
    Secure the application further using HTTPS and other security practices.
    Customize the application's appearance and functionality according to your requirements.

License

This project is licensed under the MIT License. See the LICENSE file for details.
