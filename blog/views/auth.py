from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from blog.extensions import db
from blog.forms.user import UserRegisterForm, UserLoginForm
from blog.models import User

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=('GET',))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    form = UserLoginForm(request.form)

    return render_template(
        'auth/login.html',
        form=form
    )


@auth.route('/login', methods=('POST',))
def login_post():
    form = UserLoginForm(request.form)
    user = User.query.filter_by(email=form.email.data).first()

    if not user or not check_password_hash(user.password, form.password.data):
        flash('Check your login details')
        return redirect(url_for('.login'))

    login_user(user)
    return redirect(url_for('user.profile', pk=user.id))


@auth.route('/register', methods=['GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    form = UserRegisterForm(request.form)

    return render_template('auth/register.html', form=form)


@auth.route('/register', methods=['POST'])
def register_post():
    form = UserRegisterForm(request.form)
    errors = []
    if User.query.filter_by(email=form.email.data).count():
        form.email.errors.append('Email not uniq')
        return render_template('auth/register.html', form=form)

    user = User(
        username=form.username.data,
        first_name=form.first_name.data,
        last_name=form.last_name.data,
        email=form.email.data,
        password=generate_password_hash(form.password.data)
    )

    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        errors.append('Unexpected error. Try again.')
        return render_template('auth/register.html', form=form, errors=errors)
    else:
        login_user(user)
        return redirect(url_for('user.profile', pk=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
