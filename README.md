# AuthFlask Application

AuthFlask is a web application designed to practice authentication with Flask and other libraries. This project demonstrates the use of Flask, SQLAlchemy, Flask-Migrate, WTForms, and SQLite to build a simple CRUD-based web app.
---

## Installation

### Prerequisites
Ensure you have Python (3.7 or higher) and `pip` installed on your machine.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pawadopt.git
   cd pawadopt

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   venv\Scripts\activate
   
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   
6. Initialize the database:
   ```bash
   export FLASK_APP=app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   
8. Run the application:
   ```bash
   flask run
