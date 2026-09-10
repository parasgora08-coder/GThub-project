from pathlib import Path
import sqlite3

from flask import Flask, jsonify, redirect, render_template, request, url_for


BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "contacts.db"

app = Flask(__name__, template_folder=str(BASE_DIR), static_folder=str(BASE_DIR), static_url_path="/static")


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                phone_type TEXT DEFAULT 'Mobile',
                email TEXT NOT NULL DEFAULT '',
                address TEXT NOT NULL DEFAULT '',
                city TEXT DEFAULT '',
                country TEXT DEFAULT '',
                company TEXT DEFAULT '',
                job_title TEXT DEFAULT '',
                category TEXT DEFAULT ''
            )
            """
        )


@app.route("/")
def index():
    with get_connection() as connection:
        contacts = connection.execute(
            "SELECT id, name, phone, phone_type, email, address, city, country, company, job_title, category FROM contacts ORDER BY name COLLATE NOCASE"
        ).fetchall()
    return render_template("index.html", contacts=contacts)


@app.post("/add")
def add_contact():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    phone_type = request.form.get("phone_type", "Mobile").strip()
    email = request.form.get("email", "").strip()
    address = request.form.get("address", "").strip()
    city = request.form.get("city", "").strip()
    country = request.form.get("country", "").strip()
    company = request.form.get("company", "").strip()
    job_title = request.form.get("job_title", "").strip()
    category = request.form.get("category", "").strip()

    if name and phone:
        with get_connection() as connection:
            connection.execute(
                "INSERT INTO contacts (name, phone, phone_type, email, address, city, country, company, job_title, category) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (name, phone, phone_type, email, address, city, country, company, job_title, category),
            )
    return redirect(url_for("index"))


@app.get("/search")
def search_contacts():
    query = request.args.get("q", "").strip()
    pattern = f"%{query}%"
    with get_connection() as connection:
        contacts = connection.execute(
            """
            SELECT id, name, phone, phone_type, email, address, city, country, company, job_title, category FROM contacts
            WHERE name LIKE ? OR phone LIKE ? OR email LIKE ? OR address LIKE ? 
                OR city LIKE ? OR country LIKE ? OR company LIKE ? OR job_title LIKE ? OR category LIKE ?
            ORDER BY name COLLATE NOCASE
            """,
            (pattern, pattern, pattern, pattern, pattern, pattern, pattern, pattern, pattern),
        ).fetchall()
    return jsonify([dict(contact) for contact in contacts])


@app.get("/delete/<int:contact_id>")
def delete_contact(contact_id):
    with get_connection() as connection:
        connection.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    return redirect(url_for("index"))


initialize_database()


if __name__ == "__main__":
    app.run(debug=False)
