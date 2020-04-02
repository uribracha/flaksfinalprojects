from datetime import datetime
from flaksfinalprojects import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField,SelectMultipleField,IntegerField
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

    choose_countries=SelectMultipleField("choose country",[validators.Required],choices=choose_data)
    startYear=IntegerField("start year",[validators.Required,validators.number_range(1970,2017)])
    endYear=IntegerField("end year",[validators.Required,validators.number_range(1970,2017)])
    mode=SelectField("what do you want to compare",[validators.Required],choices=[(0,"population data only"),(1,"greenhouse data only"),(2,"ratio between greenhouse gas emission and population count "),(3,"ratio between population count and greenhouse gas emission  ")] )
    typeofgraph=SelectField("select graph type",[validators.Required],choices=[(0,"line"),(1,"bar"), (2,"hist"), (3,"box"), (4,"kde"), (5,"area"), (6,"scatter"), (7,"hexbin"),(8,"pie")])
    submit = SubmitField('Submit')




