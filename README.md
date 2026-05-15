# 📚 Track Together — Assignment Tracker

A multi-user assignment tracking web app built for the University of Lancashire Hackathon 2026.

Built by Aparna, Tabitha & Tristan.

---

## What it does

- User registration and login with session management
- Add assignments with title, module, due date, and status
- Track assignment progress (Not Started / In Progress / Completed)
- View and manage modules
- Group chat feature for collaboration between users
- Clean multi-page interface with persistent SQLite storage

---

## Tech Stack

- **Python**
- **Streamlit** — multi-page web app UI
- **SQLite** — local database for users, assignments, modules, and chat
- **Git** — version control with team collaboration

---

## Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/Taken-dot/Assignment-Tracker
cd Assignment-Tracker
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the app**

```bash
streamlit run streamlit_app.py
```

---

## Project Structure

```
├── streamlit_app.py      # Login page and entry point
├── pages/
│   ├── home_page.py      # Dashboard
│   ├── create_account.py # Registration
│   └── ...               # Other pages
├── database.py           # Database setup and helpers
├── header.py             # Shared UI header component
└── requirements.txt
```

---

## Built at

University of Lancashire Hackathon 2026
