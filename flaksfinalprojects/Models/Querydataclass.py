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
#defining query form

class Querydataclass(FlaskForm):    
    #calling dataframe for country data
    df = pd.read_csv(path.join(app.root_path,"static\\Data\\greenhouse gas.csv"))
    #list used for handing select field data
    choose_data = []
    for country in df["Country"].unique():
        #filling data with all country (type tuple)
       choose_data.append((country,country))
#select field for country
    choose_countries=SelectMultipleField("choose country",[validators.Required],render_kw={"class":"form-control"},choices=choose_data)
    #integer field for starting year (note for myself: need to fix validator number range)
    startYear=IntegerField("start year",[validators.Required,validators.number_range(1970,2017)],render_kw={"class":"form-control"})
    #integer field end year (note for myself: need to fix validator number range)
    endYear=IntegerField("end year",[validators.Required,validators.number_range(1970,2017)],render_kw={"class":"form-control"})
    #selecting mode
    mode=SelectField("what do you want to compare",[validators.Required],render_kw={"class":"form-control"},choices=[("population data only","population data only"),("greenhouse data only","greenhouse data only"),("ratio between greenhouse gas emission and population count","ratio between greenhouse gas emission and population count"),("ratio between population count and greenhouse gas emission","ratio between population count and greenhouse gas emission")])
    #selecting graph size
    size=IntegerField("size of graph (inch)",[validators.Required],render_kw={"class":"form-control"})
    #selecting graph title
    title=TextField("graph title",[validators.Required],render_kw={"class":"form-control"})
    #submit 
    submit = SubmitField('Submit',render_kw={"class":"btn btn-primary"})




