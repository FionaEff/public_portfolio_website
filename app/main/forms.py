from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):

    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=100)])
    email = EmailField("Email", validators=[DataRequired(), Email(), Length(max=254)])
    subject = StringField("Subject", validators=[DataRequired(), Length(min=3, max=150)])
    message = TextAreaField("Message", validators=[DataRequired(), Length(min=10, max=5000)])
    submit = SubmitField("Send Message")
