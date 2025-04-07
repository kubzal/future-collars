# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"

# Configure SQLAlchemy with SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "tasks.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


# Define Task model
class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.Date)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.title}>"


# Create the initial database
with app.app_context():
    db.create_all()


# Routes
@app.route("/")
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)


@app.route("/task/new", methods=["GET", "POST"])
def new_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        due_date_str = request.form.get("due_date")
        due_date = (
            datetime.strptime(due_date_str, "%Y-%m-%d").date() if due_date_str else None
        )

        task = Task(title=title, description=description, due_date=due_date)
        db.session.add(task)
        db.session.commit()

        flash("Task created successfully!", "success")
        return redirect(url_for("index"))

    return render_template("new_task.html")


@app.route("/task/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/task/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted!", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
