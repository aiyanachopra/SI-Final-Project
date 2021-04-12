import requests
import csv
import json

def sampleAPI(locID, year, month, day):
    url = 'https://www.metaweather.com/api/location/' + str(locID) + '/' + str(year) + '/' + str(month) + '/' + str(day) + '/' #input as year month day
    r = requests.get(url)

    j = (r.json())
    print(j[0]) #use this to get full list of variables api gets 
    print((j[0].get('air_pressure'))) # can plug in any other variable there

for i in range(1,28):
    locID = 2459115
    year = '2020'
    day = '2'
    month = '2'
    sampleAPI(locID, year, month, str(i))