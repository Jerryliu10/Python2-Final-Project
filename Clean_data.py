# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:06:18 2020

@author: yangh
"""

import pandas as pd
df = pd.read_csv('covid_us_county.csv')

# Select out 3 representative dates 
df = df[(df["date"] == "2020-01-31") | (df["date"] == "2020-05-28") | (df["date"] == "2020-11-30")]

# df = df.iloc[:1000]
# Transform fips code into 5 digit string
df = df[(df["fips"] > 1000) & (df["fips"] < 72154)]

for i in range(len(df)):
    if df.iloc[i, 0] < 10000:
        fips_int = int(df.iloc[i, 0])
        df.iloc[i, 0] = '0' + str(fips_int)

# Export the data
df.to_csv(r"C:\Users\yangh\Documents\2020 Fall Class\Python 2\Final Project\covid_cleaned.csv", index = False)

# Take a look at the graph
# This is the graph for date "2020-11-30"
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
    
import plotly.express as px

fig = px.choropleth(df, geojson=counties, locations='fips', color='cases',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="usa",
                           labels={'cases':'cases'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()



df1 = pd.read_csv('covid_cleaned.csv')
