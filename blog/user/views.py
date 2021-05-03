from flask import Blueprint, render_template

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
    user = USERS[pk]
    return render_template(
        'users/details.html',
        username=user
    )
