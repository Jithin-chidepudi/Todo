# ✅ Todo – Full-Stack Practice App

A minimal yet modern task manager built to learn the classic web stack:

- **Back-end**: Python Flask REST API  
- **Front-end**: Vanilla JS + fetch  
- **Database**: SQLite (auto-created)  
- **Styling**: Dark-themed, responsive CSS (no frameworks)

---

## 🖥️ Preview
![screenshot](https://github.com/Jithin-chidepudi/Todo/issues/1#issue-3553434534)

---

## ⚙️ Run It Locally (2 min)

1. Clone
   ```bash
   git clone https://github.com/Jithin-chidepudi/todo.git
   cd todo

2. Start the API

cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# mac/Linux
source venv/bin/activate

pip install -r requirements.txt
python app.py          # http://localhost:5000

3. Start the UI (New Terminal)

cd frontend
python -m http.server 8000   # or Live-Server in VS Code

Open http://localhost:8000

API ENDPOINTS
| Method | Endpoint    | Description         |
| ------ | ----------- | ------------------- |
| GET    | /tasks      | List all tasks      |
| POST   | /tasks      | Create task         |
| PUT    | /tasks/{id} | Update title/status |
| DELETE | /tasks/{id} | Remove task         |

JSON Body example (POST/tasks):

{
  "title": "Buy milk",
  "due_date": "2025-11-05"
}

🧱 Project Layout

todo/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   └── app.js
└── README.md

📝 License

MIT – feel free to fork and hack away.  