Aravind Library Management System

A console-based Library Management System built using Python and Object-Oriented Programming (OOP) principles.
This project simulates real-world library operations such as book management, member registration, borrowing/returning books, overdue tracking, and data persistence.

🚀 Features

📖 Add, view, search, borrow, and return books

👤 Register and manage library members

⏰ Due-date tracking and overdue detection

💰 Overdue fine calculation (per day)

💾 Persistent storage using JSON files

🧱 Clean OOP design with separation of concerns

🧪 Unit testing support (pytest-ready)

🧑‍💼 Admin login (basic authentication)

🛠️ Tech Stack

Language: Python 3

Concepts: Object-Oriented Programming (OOP)

Modules Used: datetime, json

Testing: pytest (optional)

Data Storage: JSON files

📂 Project Structure
week5-library-system/
│── library_system/
│   ├── __init__.py
│   ├── book.py
│   ├── member.py
│   ├── library.py
│   └── main.py
│
│── data/
│   ├── books.json
│   ├── members.json
│   └── backup/
│
│── tests/
│   ├── test_book.py
│   ├── test_member.py
│   └── test_library.py
│
│── requirements.txt
│── README.md
│── .gitignore
