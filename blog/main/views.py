from flask import Blueprint, render_template

main = Blueprint('main', __name__, static_folder='../static', url_prefix='/')


@main.route('/')
def welcome():
    text = 'Hello :)'
    return render_template(
        'main/index.html',
        text=text,
    )
