from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, TextAreaField, SelectMultipleField


class CreateArticleForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired(), validators.length(10, 255)])
    text = TextAreaField('Text', [validators.DataRequired()])
    tags = SelectMultipleField('Tags', coerce=int)
    submit = SubmitField('Submit')
