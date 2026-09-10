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
                nickname TEXT DEFAULT '',
                phone TEXT NOT NULL,
                phone_type TEXT DEFAULT 'Mobile',
                alternate_phone TEXT DEFAULT '',
                email TEXT NOT NULL DEFAULT '',
                address TEXT NOT NULL DEFAULT '',
                city TEXT DEFAULT '',
                country TEXT DEFAULT '',
                company TEXT DEFAULT '',
                department TEXT DEFAULT '',
                job_title TEXT DEFAULT '',
                category TEXT DEFAULT '',
                birth_date TEXT DEFAULT '',
                website TEXT DEFAULT '',
                linkedin TEXT DEFAULT '',
                preferred_contact TEXT DEFAULT 'Phone',
                notes TEXT DEFAULT ''
            )
            """
        )


@app.route("/")
def index():
    with get_connection() as connection:
        contacts = connection.execute(
            "SELECT id, name, nickname, phone, phone_type, alternate_phone, email, address, city, country, company, department, job_title, category, birth_date, website, linkedin, preferred_contact, notes FROM contacts ORDER BY name COLLATE NOCASE"
        ).fetchall()
    return render_template("index.html", contacts=contacts)


@app.post("/add")
def add_contact():
    name = request.form.get("name", "").strip()
    nickname = request.form.get("nickname", "").strip()
    phone = request.form.get("phone", "").strip()
    phone_type = request.form.get("phone_type", "Mobile").strip()
    alternate_phone = request.form.get("alternate_phone", "").strip()
    email = request.form.get("email", "").strip()
    address = request.form.get("address", "").strip()
    city = request.form.get("city", "").strip()
    country = request.form.get("country", "").strip()
    company = request.form.get("company", "").strip()
    department = request.form.get("department", "").strip()
    job_title = request.form.get("job_title", "").strip()
    category = request.form.get("category", "").strip()
    birth_date = request.form.get("birth_date", "").strip()
    website = request.form.get("website", "").strip()
    linkedin = request.form.get("linkedin", "").strip()
    preferred_contact = request.form.get("preferred_contact", "Phone").strip()
    notes = request.form.get("notes", "").strip()

    if name and phone:
        with get_connection() as connection:
            connection.execute(
                "INSERT INTO contacts (name, nickname, phone, phone_type, alternate_phone, email, address, city, country, company, department, job_title, category, birth_date, website, linkedin, preferred_contact, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (name, nickname, phone, phone_type, alternate_phone, email, address, city, country, company, department, job_title, category, birth_date, website, linkedin, preferred_contact, notes),
            )
    return redirect(url_for("index"))


@app.get("/search")
def search_contacts():
    query = request.args.get("q", "").strip()
    pattern = f"%{query}%"
    with get_connection() as connection:
        contacts = connection.execute(
            """
            SELECT id, name, nickname, phone, phone_type, alternate_phone, email, address, city, country, company, department, job_title, category, birth_date, website, linkedin, preferred_contact, notes FROM contacts
            WHERE name LIKE ? OR nickname LIKE ? OR phone LIKE ? OR alternate_phone LIKE ? OR email LIKE ? OR address LIKE ? 
                OR city LIKE ? OR country LIKE ? OR company LIKE ? OR department LIKE ? OR job_title LIKE ? OR category LIKE ?
                OR website LIKE ? OR linkedin LIKE ? OR notes LIKE ?
            ORDER BY name COLLATE NOCASE
            """,
            (pattern, pattern, pattern, pattern, pattern, pattern, pattern, pattern, pattern, pattern, pattern, pattern, pattern, pattern, pattern),
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
