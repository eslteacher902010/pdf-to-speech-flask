from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from wtforms import StringField, SubmitField, PasswordField, TextAreaField



class MakeAList(FlaskForm):
    message = TextAreaField("Upload your pdf:", validators=[DataRequired()])
    submit = SubmitField("Submit")