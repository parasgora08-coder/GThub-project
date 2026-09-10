# 📒 Contact Book App

A comprehensive, feature-rich contact management web application built with Flask. Manage, search, and organize all your contacts in one place with an intuitive interface.

## ✨ Features

### Core Functionality
- ✅ **Add Contacts** - Store detailed information about each contact
- 🔍 **Advanced Search** - Search across multiple fields in real-time
- 📋 **View Contacts** - Display all contacts in an organized table format
- 🗑️ **Delete Contacts** - Remove contacts with confirmation prompt
- 💾 **Persistent Storage** - All data saved automatically in SQLite database

### Contact Information Fields
- **Basic Info**: Full Name, Nickname/Alias
- **Phone Details**: Primary Phone, Phone Type (Mobile/Home/Work/Other), Alternate Phone Number
- **Communication**: Email Address, Preferred Contact Method
- **Location**: Street Address, City, Country
- **Professional**: Company/Organization, Department, Job Title
- **Personal**: Birth Date, Website URL, LinkedIn Profile
- **Additional**: Category (Friend/Family/Work/Colleague/Business/Other), Notes/Comments

### Search Capabilities
Search contacts by any field:
- Name, Nickname
- Phone numbers (primary & alternate)
- Email address
- Address, City, Country
- Company, Department, Job Title
- Website, LinkedIn profile
- Category, Notes
- And more!

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.9+** | Backend runtime |
| **Flask** | Web framework |
| **SQLite** | Database |
| **HTML5** | Frontend structure |
| **CSS3** | Styling |
| **JavaScript (Vanilla)** | Dynamic search & interactivity |

## 📁 Project Structure

```
GThub-project/
├── app.py                 # Flask backend, API endpoints, database operations
├── index.html             # Main contact book UI (Jinja2 template)
├── style.css              # Responsive styling
├── cript.js               # Frontend search functionality
├── requirements.txt       # Python dependencies
├── contacts.db            # SQLite database (auto-created on first run)
└── README.md              # This file
```

## 📋 Prerequisites

- **Python 3.9 or higher**
- **pip** (Python package manager)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

## 🚀 Installation & Setup

### Step 1: Clone or Download the Project
```bash
git clone https://github.com/parasgora08-coder/GThub-project.git
cd GThub-project
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Open in Browser
Navigate to:
```
http://127.0.0.1:5000/
```

## 📖 Usage Guide

### Adding a Contact
1. Fill in the **"Add New Contact"** form
2. Required fields: Name and Phone Number
3. Optional fields: All other contact information
4. Click **"Add Contact"** button
5. Contact appears in the table below

### Searching Contacts
1. Type in the **search box** at the top
2. Results filter **in real-time** as you type
3. Search works across all contact fields
4. Clear the search box to see all contacts again

### Editing Contacts
- Currently, edit by deleting and re-adding the contact with updated information
- (Future feature: in-place editing)

### Deleting Contacts
1. Locate the contact in the table
2. Click the **"Delete"** button in the Action column
3. Confirm the deletion when prompted
4. Contact is permanently removed

## 🗄️ Database Schema

The app uses SQLite with the following contact fields:

```sql
CREATE TABLE contacts (
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
```

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Load main contact book page |
| POST | `/add` | Add a new contact |
| GET | `/search?q=<query>` | Search contacts (returns JSON) |
| GET | `/delete/<contact_id>` | Delete a contact and redirect |

## 💡 Tips & Best Practices

- 📱 Use consistent phone number formatting
- 🔖 Utilize the Category field to organize contacts by relationship
- 💬 Add notes for important information or reminders
- 📅 Set birth dates to get reminded about birthdays
- 🔗 Save LinkedIn profiles for professional networking
- 🌐 Include website URLs for easy access

## 🐛 Troubleshooting

### Port Already in Use
If port 5000 is already in use:
```bash
python app.py --port 5001
```

### Database Issues
To reset the database:
```bash
rm contacts.db
python app.py  # Creates a fresh database
```

### Module Not Found Errors
Ensure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

## 📝 Notes

- The app creates a `contacts.db` SQLite database automatically on first run
- All data is stored locally in the database file
- Search is **case-insensitive**
- The interface is **responsive** and works on desktop and tablet devices

## 🚀 Future Enhancements

- [ ] Edit existing contacts inline
- [ ] Export contacts to CSV/vCard
- [ ] Import contacts from CSV
- [ ] Advanced filtering by category
- [ ] Contact photo/avatar support
- [ ] Backup and restore functionality
- [ ] User authentication
- [ ] Mobile app version

## 📄 License

This project is for **educational and demonstration purposes**.

## 👤 Author

**Paras Gora**  
GitHub: [@parasgora08-coder](https://github.com/parasgora08-coder)

---

**Happy Contact Managing! 🎉**
