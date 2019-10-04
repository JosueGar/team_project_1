# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 19:34:33 2019

@author: rmr
"""

import requests
import json
import prettytable
import pandas as pd
from pandas.io.json import json_normalize
#naxml to dict function
file = 'data\la.areas_city.csv'


city_data =  pd.read_csv(file,index_col=False)
city_data.info()
city_data['LAU'] = 'LAU'
city_data['03'] ='03'
city_data.info()
city_data['state_and_code'] = city_data['LAU'] + city_data['PT0107000073000']+ city_data['03']

city_list = city_data['state_and_code'].tolist()
n=25
final = [city_list[i * n:(i + 1) * n] for i in range((len(city_list) + n - 1) // n )]  




cnt = 0
for x in final:
    print(cnt)
    headers = {'Content-type': 'application/json'}
    data = json.dumps({"seriesid": final[cnt],"startyear":"2014", "endyear":"2018"})
    p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
    json_data[cnt] = json.loads(p.text)
    for series in json_data['Results']['series']:
        x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
        seriesId = series['seriesID']
        for item in series['data']:
            year = item['year']
            period = item['period']
            value = item['value']
            footnotes=""
            for footnote in item['footnotes']:
                if footnote:
                    footnotes = footnotes + footnote['text'] + ','  
    cnt +=1

test_df = json_normalize(json_data[0]['Results']['series'])

test = pd.concat(
                        [(json_normalize(v[keyparent],sep='_')) 
                            for k,v in json_data.items() if k > 0 
                        ],sort=False)

n = 0    
for k,v in json_data.items():
    test[k] = json_data[v]
        
        
test = json_data[0]
    
if 'M01' <= period <= 'M12':
    x.add_row([seriesId,year,period,value,footnotes[0:-1]])
    output = open(&quot;c:\\temp\\&quot; + seriesId + &quot;.txt&quot;,&quot;w&quot;)
    output.write (x.get_string())
    output.close()
    
    
    
CS2570605000000
CS2571025000000
CS2571095000000
CS2571480000000
CS2571620000000
CS2572215000000
CS2572390000000
CS2572495000000
CS2572880000000
CS2572985000000
CS2573090000000
CS2573265000000
CS2573335000000
CS2573790000000
CS2573895000000
CS2574385000000
CS2574525000000
CS2574595000000
CS2575015000000
CS2575155000000
CS2575260000000
CS2575400000000
CS2576135000000
CS2576380000000
CS2577010000000
CS2577150000000
