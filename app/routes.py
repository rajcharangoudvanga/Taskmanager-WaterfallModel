from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Task

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    description = request.form.get('description')
    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/complete/<int:id>')
def complete(id):
    task = Task.query.get(id)
    task.status = "Completed"
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/pending/<int:id>')
def pending(id):
    task = Task.query.get(id)
    task.status = "Pending"
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    task = Task.query.get(id)
    if request.method == "POST":
        task.title = request.form.get("title")
        task.description = request.form.get("description")
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template("edit.html", task=task)
