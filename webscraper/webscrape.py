# Importing functions which allows data to be extracted
from lxml import html
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os

def graph(weather, location):
    temprange = plt.axes()
    # Alpha gives the colour density
    # Decimals control spacing between bars
    temprange.bar([1.5, 2.5, 3.5, 4.5, 5.5], weather['Min'], width=0.5, alpha=0.4)
    # if statement to control the issue of any missing data
    if len(weather['Max']) == 4:
        temprange.bar([1, 2, 3, 4], weather['Max'], width=0.5, alpha=0.4)
    elif len(weather['Max']) == 5:
        temprange.bar([1, 2, 3, 4, 5], weather['Max'], width=0.5, alpha=0.4)
    # x axis (days)
    temprange.set_xticklabels(weather['Day'])
    # y axis, auto sets from min value to max value temp
    weather=np.ma.masked_array(weather, mask=(weather==-999), fill_value=0)
    # prints the graph
    plt.show()

def weather_report(URL):
    # Pulls the desired website
    page = requests.get(URL)
   # Extracting HTML
    data = html.fromstring(page.content)
  # Extacting data from BBC weather for days, min & max temp
    day = data.xpath('//*[@id="blq-content"]/div[7]/div[2]/ul/li/a/div/h3/span/text()')
    max_temp = data.xpath('//*[@id="blq-content"]/div[7]/div[2]/ul/li/a/span[2]/span/span[1]/text()')
    min_temp = data.xpath('//*[@id="blq-content"]/div[7]/div[2]/ul/li/a/span[3]/span/span[1]/text()')
    location = data.xpath('//*[@id="blq-content"]/div[1]/h1/span/text()')
    print (location[0] + " five day forecast")
# When max temp for nightime is missing...
    if len(max_temp) == 4:
        weather=-999*np.ones((5,3), dtype='object') # Deals with the missing data issue, sets any missing temp as -999
        weather[:,0] = day
        # Note that this is different from the elif statement below: [1:,1] instead of [:,1]. Handling the missing data issue
        weather[1:,1] = [int(i) for i in max_temp]
        weather[:,2] = [int(i) for i in min_temp]
    # If the length of max list is 5 (i.e. it's daytime) do this:
    elif len(max_temp) == 5:
        weather=np.zeros((5,3), dtype='object')
        weather[:,0] = day
        weather[:,1] = [int(i) for i in max_temp]
        weather[:,2] = [int(i) for i in min_temp]
  # Masks any -999 in weather, fill value means to blank them out
    weather=np.ma.masked_array(weather, mask=(weather==-999), fill_value=0)
    weather = pd.DataFrame(weather, columns=['Day', 'Max', 'Min']) # Labels the columns

    #root = "/home/grace/Desktop/Web Scraper Project/"
    #weather = pd.DataFrame(weather, columns=['Day', 'Max', 'Min']) # Labels the columns
    #filename = city[0] + ".csv"
    #with open(root + filename, "a") as f:
       # weather.to_csv(f, header=False) # Appending so that we can collect data over time
    #weather.to_csv(city[0] + ".csv") Magic one line code for making a csv file
    #make_graph(weather, city)

    root = "/home/sylke/Desktop/webscraper/"
    filename = location[0] + ".csv"
    with open(root + filename, "a") as d:
        weather.to_csv(d, header=False)
   # weather.to_csv = location[0] + ".csv")
    print (weather)
    # graph(weather, location)

Las_vegas_temp = 'http://www.bbc.co.uk/weather/5506956'
Purley_temp = 'http://www.bbc.co.uk/weather/2639842'
Amsterdam_temp = 'http://www.bbc.co.uk/weather/2759794'

weather_report(Las_vegas_temp)
weather_report(Purley_temp)
weather_report(Amsterdam_temp)
