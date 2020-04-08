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
       choose_data.append((country,country))

    choose_countries=SelectMultipleField("choose country",[validators.Required],render_kw={"class":"form-control"},choices=choose_data)
    startYear=IntegerField("start year",[validators.Required,validators.number_range(1970,2017)],render_kw={"class":"form-control"})
    endYear=IntegerField("end year",[validators.Required,validators.number_range(1970,2017)],render_kw={"class":"form-control"})
    mode=SelectField("what do you want to compare",[validators.Required],render_kw={"class":"form-control"},choices=[("population data only","population data only"),("greenhouse data only","greenhouse data only"),("ratio between greenhouse gas emission and population count","ratio between greenhouse gas emission and population count"),("ratio between population count and greenhouse gas emission","ratio between population count and greenhouse gas emission")])
    size=IntegerField("size of graph (inch)",[validators.Required],render_kw={"class":"form-control"})
    title=TextField("graph title",[validators.Required],render_kw={"class":"form-control"})
    submit = SubmitField('Submit',render_kw={"class":"btn btn-primary"})




