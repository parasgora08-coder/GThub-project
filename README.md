# Contact Book App

A simple contact management web application built with Flask. It lets you add, search, and delete contacts through a clean browser interface.

## Features

- Add new contacts with name, phone, email, and address
- Search contacts by name, phone, email, or address
- View all saved contacts in a table
- Delete contacts from the list
- Stores data in a SQLite database automatically

## Tech Stack

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript

## Project Structure

- `app.py` — Flask backend and database setup
- `index.html` — main contact book UI
- `style.css` — page styling
- `cript.js` — frontend search behavior
- `requirements.txt` — Python dependencies
- `contacts.db` — SQLite database created when the app runs

## Prerequisites

- Python 3.9+
- pip

## Installation

1. Open a terminal in the project folder.
2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

Start the Flask app:

```bash
python app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000/
```

## Usage

- Fill in the form to add a contact.
- Use the search box to filter contacts in real time.
- Click the Delete button next to any contact to remove it.

## Notes

The app creates a SQLite database named `contacts.db` automatically on first run if it does not already exist.

## License

This project is for educational/demo use.
