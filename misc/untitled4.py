# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:08:55 2019

@author: rmr
"""
import requests
import json
import prettytable
import pandas as pd
from pandas.io.json import json_normalize


headers = {'Content-type': 'application/json'}
    data = json.dumps({"seriesid": final[cnt],"startyear":"2014", "endyear":"2018"})
    p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
    json_data[cnt] = json.loads(p.text)
https://api.bls.gov/publicAPI/v2/surveys


survey_dict = {}
url = "https://api.bls.gov/publicAPI/v2/surveys"
units = "imperial"
query_url = f"{url}"
response = requests.get(query_url).json()

test = json_normalize(response['Results']['survey'])

for i in len(response):
    survey_dict['survey'][] = response['Results']['Survey'][i]
        }

print(f"Processing Record {cnt} of Set {setof} | {city}")
try:
    city_dict[city]={'Cloudiness':(response['clouds']['all'])
                     ,'Country':(response['sys']['country'])
                     ,'Date':(response['dt'])
                     ,'Humidity':(response['main']['humidity'])
                     ,'Lat':(response['coord']['lat'])
                     ,'Lng':(response['coord']['lon'])
                     ,'Max Temp':(response['main']['temp_max'])
                     ,'Wind Speed':(response['wind']['speed'])
                    }
    
la_area_codes = pd.read_csv('data/la.area.codes.txt', sep='\t')

import quandl
quandl.ApiConfig.api_key = '9urisjjRCGFkqV5SGLDs'

quandl.get('ZILLOW/M1300_MPPRSF', start_date='2019-01-31', end_date='2019-01-31')