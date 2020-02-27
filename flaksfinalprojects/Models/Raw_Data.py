import pandas as pd
import numpy as np
from os import path
class Raw_Data_pop(object):
    def get_pop_Raw():
        df = pd.read_csv( "C:\\Users\\User\\source\\repos\\flaksfinalprojects\\flaksfinalprojects\\static\\Data\\population_data.csv")
        df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        raw_data_table_pop = df.to_html(classes = 'table table-hover')
        return raw_data_table_pop
    def get_gas_Raw(): 
        df1 = pd.read_csv( "C:\\Users\\User\\source\\repos\\flaksfinalprojects\\flaksfinalprojects\\static\\Data\\greenhouse gas.csv")
        df1.drop(df1.columns[df1.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        raw_data_table_gas = df1.to_html(classes = 'table table-hover')
        return raw_data_table_gas
    