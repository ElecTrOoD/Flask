from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, static_folder='../static', url_prefix='/user')

USERS = {
    1: 'Alice',
    2: 'John',
    3: 'Mike'
}


@user.route('/')
def user_list():
    return render_template(
        'users/user_list.html',
        users_list=USERS,
    )


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user = USERS[pk]
    except KeyError:
        raise NotFound(f'User with id {pk} not found.')
    return render_template(
        'users/details.html',
        username=user
    )
