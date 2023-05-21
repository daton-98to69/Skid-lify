from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

list = ["ankit", "sibam"]


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()  # You could do id=id
        if user:
            # For email, we do user.email --- database
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!', category='success')
                # This makes sure web browser remembers user
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", text=list[1], text1=list[0], user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        password1 = request.form.get('password1')

        # Checking if user already exist
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category='error')
        elif len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif len(username) < 2:
            flash("Username must be greater than 2 characters", category="error")
        elif password != password1:
            flash("Password don\'t match.", category="error")
        elif len(password1) < 7:
            flash("Password must be atleast 7 characters", category="error")
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created!", category="success")
            # We could use /home but it is better to say views.home so that if we ever change the route it will still work.
            return redirect(url_for('views.home'))

    return render_template("sign-up.html", user=current_user)