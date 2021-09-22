import json
import pickle
import numpy as np
import pandas as pd
import datetime

__data_columns = None
__model = None

def get_power_consumption(year,month,day,temp_max,dew_max):
    print("Predictions...start")
    df_date = pd.DataFrame({'year': [year],
                            'month': [month],
                            'day': [day], 'temp_max': [float(temp_max)], 'dew_max': [float(dew_max)]})
    df_date['date'] = pd.to_datetime(df_date[["year", "month", "day"]])
    return round(__model.predict(start=df_date.iloc[0]['date'], end=df_date.iloc[0]['date'], exog=df_date[['temp_max','dew_max']])[0],2)


def get_col_names():
    return __data_columns

def load_saved_artifacts():
    print("loading saved artifacts..start")
    global __data_columns
    global __model

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']

    with open("./artifacts/House_Power_Consumption_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_col_names())
    print(get_power_consumption(2019, 8, 1, 25, 12))
    print(get_power_consumption(2019, 8, 1, 125, 100))