"""
Routes and views for the flask application.
"""
from flask import flash

import pandas as pd
import numpy as np
from datetime import datetime
from flask import render_template
from flaksfinalprojects import app
from flaksfinalprojects.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines
from flask import render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flaksfinalprojects.Models.QueryFormStructure import QueryFormStructure 
from flaksfinalprojects.Models.QueryFormStructure import LoginFormStructure 
from flaksfinalprojects.Models.QueryFormStructure import UserRegistrationFormStructure 
from flaksfinalprojects.Models.Raw_Data import Raw_Data_pop

from flaksfinalprojects.Models.Forms import ExpandForm
from flaksfinalprojects.Models.Forms import CollapseForm

db_Functions = create_LocalDatabaseServiceRoutines() 
@app.route('/')
@app.route('/home')
def home():
    return render_template(
        "index.html"
        )
    """Renders the home page."""
    

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='contect details'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='my application about page'
    )
@app.route("/data")
def data():
    return render_template(
           'Data.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
        )
@app.route('/Greenhousegasdata',methods = ['GET' , 'POST'])


def Greenhousegasdata():
    form1 = ExpandForm()
    form2 = CollapseForm()
    raw_data_table = ''
    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = Raw_Data_pop.get_gas_Raw()
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''
        

    """Renders the contact page."""
    return render_template(
        'dataGreenhouse.html',
        title='greenhouse gas data',
        year=datetime.now().year,
        message='Your contact page.',
        data=raw_data_table,
        form1=form1,
        form2=form2
    )


@app.route('/populationdata',methods = ['GET' , 'POST'])

def populationdata():
    form1 = ExpandForm()
    form2 = CollapseForm()
    raw_data_table = ''
    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = Raw_Data_pop.get_pop_Raw()
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    """Renders the contact page."""
    return render_template(
        'dataPopulation.html',
        title='greenhouse gas data',
        year=datetime.now().year,
        message='Your contact page.',
        datapop=raw_data_table,
        form1=form1,
        form2=form2
     
    ) 
@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            return redirect('/login')
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

# -------------------------------------------------------
# Login page
# This page is the filter before the data analysis
# -------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            return redirect('/data')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )
@app.route("/picturealbum")
def picturealbum():
    return render_template(
        "picturealbum.html",
        title="power plant pictures",
      
        )
