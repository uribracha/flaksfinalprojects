from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import validators, ValidationError

from wtforms.validators import DataRequired
class Querydataclass(FlaskForm):
    first_country=StringField("first country for checking",[validators.required("please put country"),validators.Length(2,message="please put valid country")])
    second_country=StringField("second country for checking")
    whattotest=SelectField("what to test", choices=[("greenhouse","only greenhouse gas"),("pop","only population"),("pop and greenhouse","both population and greenhouse gas")],validators=[validators.required("please put country")])
    yearstart=DateField('Start year', format='%m/%d/%Y')
    yearEnd=DateField('End Year', format='%m/%d/%Y')
    submit = SubmitField('Submit')




