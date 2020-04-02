from datetime import datetime
from flaksfinalprojects import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField,SelectMultipleField
from wtforms import validators, ValidationError
import pandas as pd
import numpy as np
from os import path
import sys

from wtforms.validators import DataRequired
class Querydataclass(FlaskForm):
    df = pd.read_csv(path.join(app.root_path,"static\\Data\\greenhouse gas.csv"))
    choose_data = []
    for index,country in enumerate(df["Country"].unique()):
       choose_data.append((index,country))
    submit = SubmitField('Submit')
choose_countries=SelectMultipleField("choose country",choices=choose_data,[validators.Required])
startYear=IntegerField("start year",[validators.Required,validators.number_range(1970,2017)])
endYear=IntegerField("end year",[validators.Required,validators.number_range(1970,2017)])
mode=SelectField("what do you want to compare",choices=[(0,"population data only"),(1,"greenhouse data only"),(2,"ratio between greenhouse gas emission and population count "),(3,"ratio between population count and greenhouse gas emission  ")] [validators.Required])
typeofgraph=SelectField("select graph type",choices=[(0,"bar"), (1,"hist"), (2,"box"), (3,"kde"), (4,"area"), (5,"scatter"), (6,"hexbin"),(7,"pie")] [validators.Required])




