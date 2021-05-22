from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

from blog.app import db

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')

    email = request.form.get('email')
    password = request.form.get('password')

    from blog.models import User

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Incorrect login or password')
        return redirect(url_for('.login'))

    login_user(user)
    return redirect(url_for('user.profile', pk=user.id))


@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    from blog.models import User

    db.session.add(
        User(username=name,
             email=email,
             password=generate_password_hash(password)))
    db.session.commit()

    user = User.query.filter_by(email=email).first()

    login_user(user)
    return redirect(url_for('user.profile', pk=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
