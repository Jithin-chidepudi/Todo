from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)
CORS(app)

class Task(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    title    = db.Column(db.String(120), nullable=False)
    status   = db.Column(db.String(20), default="pending")
    due_date = db.Column(db.Date, nullable=True)

# ---- REST endpoints ----
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify([{"id": t.id, "title": t.title, "status": t.status, "due_date": str(t.due_date)}
                    for t in Task.query.all()])

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    new = Task(title=data["title"],
               due_date=datetime.strptime(data["due_date"], "%Y-%m-%d").date() if data.get("due_date") else None)
    db.session.add(new)
    db.session.commit()
    return jsonify(id=new.id), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json
    if "title" in data: task.title = data["title"]
    if "status" in data: task.status = data["status"]
    if "due_date" in data:
        task.due_date = datetime.strptime(data["due_date"], "%Y-%m-%d").date() if data["due_date"] else None
    db.session.commit()
    return "", 204

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    Task.query.filter_by(id=task_id).delete()
    db.session.commit()
    return "", 204

# create DB tables on first run
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=5000)