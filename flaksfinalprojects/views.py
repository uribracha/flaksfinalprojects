"""
Routes and views for the flask application.
"""
from flask import flash
from os import path
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

from flaksfinalprojects.Models.QueryFormStructure import LoginFormStructure 
from flaksfinalprojects.Models.QueryFormStructure import UserRegistrationFormStructure 
from flaksfinalprojects.Models.Forms import ExpandForm
from flaksfinalprojects.Models.Forms import CollapseForm
from flaksfinalprojects.Models.Querydataclass import Querydataclass
from flaksfinalprojects.Models.queryfunctions import queryfunctions
import sys

db_Functions = create_LocalDatabaseServiceRoutines() 
@app.route('/')
@app.route('/home')
def home():
    return render_template(
        "index.html"
        )
    """Renders the home page."""
    

@app.route('/contact')
#this is contact page
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='contect details'
    )

@app.route('/about')
#this is about page
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='my application about page'
    )
@app.route("/data")
#this is the data page(page of table review)

def data():
    return render_template(
           'Data.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
        )
@app.route('/Greenhousegasdata',methods = ['GET' , 'POST'])

#indivdual page of table review (greenhouse)
def Greenhousegasdata():
    form1 = ExpandForm()
    form2 = CollapseForm()
    df1 = pd.read_csv( path.join(path.dirname(__file__), 'static\\Data\\greenhouse gas.csv'))
    df1.drop(df1.columns[df1.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    raw_data_table_gas = df1.to_html(classes = 'table table-hover')
    
    
    raw_data_table = ''
    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = raw_data_table_gas
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''
        

    
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
#indivdual page of table review (population)
def populationdata():
    #reading dataframe

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\population_data.csv'))
    #dropping  columns that are not needed

    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    
    raw_data_table_pop = df.to_html(classes = 'table table-hover')
    form1 = ExpandForm()
    form2 = CollapseForm()
    raw_data_table = ''
    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = raw_data_table_pop
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

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
    #checking post and form validition
    if (request.method == 'POST' and form.validate()):
        #checking if username and password exist (see QueryFormStructure)
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            return redirect('/query')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )
#picture album
@app.route("/picturealbum")
def picturealbum():
    return render_template(
        "picturealbum.html",
        title="power plant pictures",
      
        )
@app.route('/query',methods=['GET', 'POST'])
#query
def query():
    #define starting variable
    chart=''
    table=''
    
    form=Querydataclass(request.form)
    #checking post
    if request.method=="POST":
        #finding what function to use see queryfuncations page to see funcation review.

        if form.mode.data=="population data only":
            #calling proper function from queryfunctions
          result=queryfunctions.population_only(queryfunctions,form.choose_countries.data , form.startYear.data , form.endYear.data,form.size.data,form.title.data)
          table=result["table"]

          chart=result["chart"]

        elif form.mode.data=="greenhouse data only":
             #calling proper function from queryfunctions
          result=queryfunctions.greenhousegasonly(queryfunctions,form.choose_countries.data , form.startYear.data , form.endYear.data,form.size.data,form.title.data)

          table=result["table"]

          chart=result["chart"]

        elif form.mode.data=="ratio between greenhouse gas emission and population count":
             #calling proper function from queryfunctions
            result=queryfunctions.ratiogastopopulation(queryfunctions,form.choose_countries.data , form.startYear.data , form.endYear.data,form.size.data,form.title.data)
            
            table=result["table"]

            chart=result["chart"]

        elif form.mode.data=="ratio between population count and greenhouse gas emission":
             #calling proper function from queryfunctions
            result=queryfunctions.ratiopopulationtogas(queryfunctions,form.choose_countries.data , form.startYear.data , form.endYear.data,form.size.data,form.title.data)

            table=result["table"]

            chart=result["chart"]
          
    return render_template(
    "QueryData.html",
    title="query the dataset",
    form=form,
    table=table,
    chart=chart
    )
    

      
        