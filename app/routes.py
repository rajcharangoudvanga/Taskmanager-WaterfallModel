from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from .models import Task, User
from .forms import RegistrationForm, LoginForm

main = Blueprint('main', __name__)

# ---------------- Auth Routes ----------------

@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful! Please login.", "success")
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("main.index"))
        flash("Invalid email or password", "danger")
    return render_template("login.html", form=form)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))

# ---------------- Task Routes ----------------

@main.route('/')
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['POST'])
@login_required
def add():
    title = request.form.get('title')
    description = request.form.get('description')
    task = Task(title=title, description=description, user_id=current_user.id)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:id>', methods=['POST']) 
@login_required
def delete(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash("You are not allowed to delete this task.", "danger")
        return redirect(url_for('main.index'))
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/complete/<int:id>', methods=['POST']) 
@login_required
def complete(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash("Not authorized.", "danger")
        return redirect(url_for('main.index'))
    task.status = "Completed"
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/pending/<int:id>', methods=['POST'])
@login_required
def pending(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash("Not authorized.", "danger")
        return redirect(url_for('main.index'))
    task.status = "Pending"
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash("Not authorized.", "danger")
        return redirect(url_for('main.index'))
    if request.method == "POST":
        task.title = request.form.get("title")
        task.description = request.form.get("description")
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template("edit.html", task=task)
