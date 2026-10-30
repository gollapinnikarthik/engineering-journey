User Registration Validation
Project Overview
A Python learning project that validates user registration details, including usernames, email addresses, and passwords.
The project demonstrates reusable functions, input validation, exception handling, nested dictionaries, and testing.
Project Structure
user-registration-validation/
├── python_functions.py
├── registration.py
├── test_registration.py
├── README.md
└── .gitignore
Features
1. Username Validation
The validate_name() function checks that:
The input is a string.
The username contains at least 3 characters.
Whitespace is not allowed.
Only alphanumeric characters, periods, and underscores are permitted.
Periods cannot appear at the beginning or end.
Consecutive periods are not allowed.
2. Email Validation
The validate_email() function checks that:
The input is a string.
Exactly one @ symbol is present.
The username portion contains at least 2 characters.
The domain contains at least one period.
Domain sections cannot be empty.
Whitespace is not allowed.
3. Password Validation
The validate_password() function checks that:
The input is a string.
The password contains at least 8 characters.
At least one uppercase letter is present.
At least one lowercase letter is present.
At least one digit is present.
At least one allowed special character is present.
Whitespace is not allowed.
Allowed special characters: ! @ # $ % ^ & *
4. User Registration
The registration module:
Uses the reusable validation functions.
Raises ValueError when validation fails.
Handles exceptions and displays validation messages.
Returns the registered user data on success.
Returns False when registration fails.
Running the Project
From the project directory:
python3 test_registration.py
Python Concepts Practiced
Functions and return values
Boolean operators and short-circuit evaluation
String methods and membership operators
Lists, sets, and nested dictionaries
For loops and Boolean flags
Guard clauses and early returns
Type checking using isinstance()
Raising and handling exceptions
Modular programming and imports
Debugging, edge-case testing, and refactoring
Future Improvements
Secure password hashing using established libraries
Longer passphrases and compromised-password checks
Database integration
Duplicate username and email detection
Automated unit tests using pytest
API-based registration
Improved error handling and input normalization
Disclaimer
This is an educational Python project, not a production-ready authentication system. It uses fictional registration data to demonstrate programming concepts. Real applications must securely hash passwords and avoid storing or exposing plaintext credentials.