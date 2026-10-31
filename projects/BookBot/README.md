# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

BookBot is a command-line Python application that analyzes text files and generates a report containing word counts and character frequencies.
Built independently as part of the Boot.dev BookBot project.
Features
Reads text files using Python’s with open().
Counts the total number of words.
Counts character occurrences, ignoring case.
Includes spaces, punctuation, and symbols in character counting.
Sorts characters by frequency in descending order.
Displays alphabetic character frequencies in a formatted report.
Accepts a book’s file path as a command-line argument.
Displays usage instructions when a required argument is missing.
Project Structure
BookBot/
├── main.py
├── stats.py
├── books/
│   └── frankenstein.txt
└── README.md
How to Run
Clone the repository and navigate to the BookBot directory.
cd projects/BookBot
Run BookBot with a text file:
python3 main.py books/frankenstein.txt
You can analyze another book by passing its file path:
python3 main.py books/another_book.txt
If no book path is provided, BookBot displays:
Usage: python3 main.py <path_to_book>
The program exits with status code 1.
Python Concepts Practiced
Functions and parameters
Return values and type hints
File handling with with open()
String manipulation using .split() and .lower()
Dictionaries and character-frequency counting
Dictionary iteration with .items()
Lists and tuples
Tuple unpacking
Sorting with sorted(), key, and reverse
Passing functions as arguments
Conditional statements and loops
.isalpha() for character filtering
Command-line arguments using sys.argv
Program termination using sys.exit()
Modular programming and imports
Debugging and testing
Future Improvements
Support multiple book files in one execution.
Export reports to text or CSV files.
Add automated tests.
Handle missing or unreadable files gracefully.
Compare word and character frequencies across books.
Learning Objective
The primary goal of this project was to implement a complete Python application from scratch, practice debugging independently, and strengthen foundational programming skills.
The project prioritizes understanding, correctness, and readable code over premature optimization.