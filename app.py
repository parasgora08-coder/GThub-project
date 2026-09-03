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
                email TEXT NOT NULL DEFAULT '',
                address TEXT NOT NULL DEFAULT ''
            )
            """
        )


@app.route("/")
def index():
    with get_connection() as connection:
        contacts = connection.execute(
            "SELECT id, name, phone, email, address FROM contacts ORDER BY name COLLATE NOCASE"
        ).fetchall()
    return render_template("index.html", contacts=contacts)


@app.post("/add")
def add_contact():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    email = request.form.get("email", "").strip()
    address = request.form.get("address", "").strip()

    if name and phone:
        with get_connection() as connection:
            connection.execute(
                "INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                (name, phone, email, address),
            )
    return redirect(url_for("index"))


@app.get("/search")
def search_contacts():
    query = request.args.get("q", "").strip()
    pattern = f"%{query}%"
    with get_connection() as connection:
        contacts = connection.execute(
            """
            SELECT id, name, phone, email, address FROM contacts
            WHERE name LIKE ? OR phone LIKE ? OR email LIKE ? OR address LIKE ?
            ORDER BY name COLLATE NOCASE
            """,
            (pattern, pattern, pattern, pattern),
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
