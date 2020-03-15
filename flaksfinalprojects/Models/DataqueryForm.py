from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import validators, ValidationError

from wtforms.validators import DataRequired
class DataqueryForm(object):
    first_country=TextField("first country for checking",[validators.required("please put country"),validators.Length(2,message="please put valid country")])


