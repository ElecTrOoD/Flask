from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, TextAreaField


class CreateArticleForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired(), validators.length(10, 255)])
    text = TextAreaField('Text', [validators.DataRequired()])
    submit = SubmitField('Submit')
