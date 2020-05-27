import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import base64
from os import path
import io

from flaksfinalprojects import app

class queryfunctions(object):
    # this class handles the functionalty of the form response see querydataclass for the form itself
    """description of class"""
# population data option 
    def population_only(self,countries,startYear,endYear,size,title):
       r={} # this dictonary hold the data returned to the view
       pop_df =pd.DataFrame( pd.read_csv(path.join(app.root_path,"static\\Data\\population_data.csv"),index_col=0)) # loading the dataframe
       df_final=pd.DataFrame(pop_df[(pop_df["Year"]>=startYear) & (pop_df["Year"]<=endYear) & (pop_df["Country"].isin(countries))]) 
       r["table"]=df_final.to_html(classes="table table-hover") 
       
       fig, ax = plt.subplots() # setting up the figure for the plot
       # groupby and chart building (costumizable fig size multipule plot in same fig )
       for name,country in df_final.groupby("Country"):
           fig.suptitle(title, fontsize=16)
           plt.ylabel("population count (Thousands)")
           country.plot(x="Year",figsize=(size, size),y="PopTotal",ax=ax, label=name)
             
          
       r["chart"]=self. plot_to_img(fig)   #save figure to img
       return r

           
#greenhouse data only built the same way see 
    def greenhousegasonly(self,countries,startYear,endYear,size,title):
        #dict
        r={}
        #calling dataframe
        
        gas_df =pd.DataFrame( pd.read_csv(path.join(app.root_path,"static\\Data\\greenhouse gas.csv"),index_col=0))

        #getting only needed data from paramter (given by form see Querydataclass.py)

        
        df_final=pd.DataFrame(gas_df[(gas_df["Year"]>=startYear) & (gas_df["Year"]<=endYear) & (gas_df["Country"].isin(countries))])
        #putting the html table in dictonary
        r["table"]=df_final.to_html(classes="table table-hover")

        fig, ax = plt.subplots()
# orgnizing graph with title from, label and then plotting
        for name,country in df_final.groupby("Country"):

            fig.suptitle(title, fontsize=16)
            plt.ylabel("Greenhouse Gas emissions (tons)")
            plot= country.plot(x="Year",figsize=(size, size),y="Value",ax=ax, label=name)

        r["chart"]=self. plot_to_img(fig)   
        return r 
    #ratio of greenhouse gas to population for refernce see ratiopopulationtogas
    def ratiogastopopulation(self,countries,startYear,endYear,size,title):

        r={}
        gas_df =pd.DataFrame( pd.read_csv(path.join(app.root_path,"static\\Data\\greenhouse gas.csv"),index_col=0))
        pop_df =pd.DataFrame( pd.read_csv(path.join(app.root_path,"static\\Data\\population_data.csv"),index_col=0))


        df_final=pop_df.merge(gas_df)
    
        df_final=(df_final[(df_final["Year"]>=startYear) & (df_final["Year"]<=endYear) & (df_final["Country"].isin(countries))])
        df_final["ratio"]=df_final["Value"]/df_final["PopTotal"]

        r["table"]=df_final.to_html(classes="table table-hover")

        fig, ax = plt.subplots()

        for name,country in df_final.groupby("Country"):
            fig.suptitle(title, fontsize=16)
            plt.ylabel("ratio between Greenhouse Gas emissions (tons) and population count (Thousands)  ")
            plot= country.plot(x="Year",figsize=(size, size),y="ratio",ax=ax, label=name)

        r["chart"]=self. plot_to_img(fig)   
        return r
    #population to gas ratio
    def ratiopopulationtogas(self,countries,startYear,endYear,size,title):
        #dictonary used for ease of acsess in views.py
        r={}
        #calling dataframe
        gas_df =pd.DataFrame( pd.read_csv(path.join(app.root_path,"static\\Data\\greenhouse gas.csv"),index_col=0))
        pop_df =pd.DataFrame( pd.read_csv(path.join(app.root_path,"static\\Data\\population_data.csv"),index_col=0))

        #merging to get all values
        df_final=pop_df.merge(gas_df)
    #ratios
        df_final=(df_final[(df_final["Year"]>=startYear) & (df_final["Year"]<=endYear) & (df_final["Country"].isin(countries))])
        df_final["ratio"]=df_final["PopTotal"]/df_final["Value"]
        # putting data in r (dict)
        r["table"]=df_final.to_html(classes="table table-hover")
        #figure creation
        fig, ax = plt.subplots()
        #grouby to get all countries in same figure
        for name,country in df_final.groupby("Country"):
            fig.suptitle(title, fontsize=16)
            plt.ylabel("ratio between population count (Thousands) and Greenhouse Gas emissions (tons)   ")
            plot= country.plot(x="Year",figsize=(size, size),y="ratio",ax=ax, label=name)
            # calling plot  to img.
        r["chart"]=self. plot_to_img(fig)   
        return r
    #function to convert figure to img (used in html)
    def plot_to_img(fig):
        pngImage = io.BytesIO()
        FigureCanvas(fig).print_png(pngImage)
        pngImageB64String = "data:image/png;base64,"
        pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
        return pngImageB64String
