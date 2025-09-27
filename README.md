# 🧾 NoteNest

**NoteNest** is a lightweight and modular Python backend for managing notes via RESTful APIs. Built with Flask and powered by JSON file storage, it offers a clean and scalable foundation for note-taking applications, prototypes, or backend learning projects.

---

## 🚀 Features

- 🧠 Create, read, update, and delete notes via RESTful endpoints
- 📁 Stores data locally in a structured `notes.json` file
- 🧩 Modular architecture with clear separation of models, services, and utilities
- 🔍 Easy to test and extend with new features or database integrations
- 🧪 Optional unit tests for core logic

---

## 📁 Project Structure

```bash
NoteNest/
├── app.py                  # Flask server and route registration
├── notes.json              # Local JSON file for storing notes
├── models/                 # Note schema and data structure
│   └── note.py
├── services/               # Business logic: create, read, update, delete
│   └── note_service.py
├── utils/                  # JSON file helpers: read/write operations
│   └── file_handler.py
├── tests/                  # Unit tests (optional)
│   └── test_notes.py
├── requirements.txt        # Python dependencies
```
📡 API Endpoints
POST /notes
Create a new note.

Request:
```
json
{
  "title": "First Note",
  "content": "This is my first note"
}
```
Response:
```
json
{
  "id": 1,
  "title": "First Note",
  "content": "This is my first note"
}
```
GET /notes
Retrieve all notes.

Sample Response:
```
json
[
  {
    "id": 1,
    "title": "First Note",
    "content": "This is my first note"
  }
]
```
** GET /notes/<id>
** Retrieve a specific note by ID.
** PUT /notes/<id>
** Update an existing note.
** DELETE /notes/<id>
** Delete a note by ID.

---
⚙️ Getting Started
1. Clone the repository
```bash
git clone https://github.com/yourusername/notenest.git
cd notenest
3. Install dependencies
bash
pip install -r requirements.txt
4. Run the server
bash
python app.py
Server will start at http://localhost:5000
```
🧠 Technologies Used
Python 3.x

Flask

JSON file storage

📌 Notes
This project is ideal for:

Backend learners exploring RESTful APIs

Quick prototyping without database setup

Extending into full-stack apps with React, Vue, or mobile frontends

✨ Author
Murad — Full-stack developer & system architect GitHub: @MuradIsazade777
