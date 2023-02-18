'''
This program uses the bing api to get latitude and longitude
for a list of cities and write them to an output file.

Author: Amanda Hanway
Date: 2/12/23

Resources:
https://pypi.org/project/geocoder/
http://geocoder.readthedocs.org/providers/Bing.html
https://stackoverflow.com/questions/13686001/python-module-for-getting-latitude-and-longitude-from-the-name-of-a-us-city
'''

import geocoder 
import csv
import sys

bing_api_key = 'AsLy66I_NnXlVlHcXGTuy63sSthj0uhwWUEUCZY69FFjtc60gXJYYiuxOdbdAPq9'
input_file = 'cities.csv'
output_file = 'cities_output.csv'
output_list = []
row_count = 0

with open(input_file, 'r') as file:
    reader = csv.reader(file, delimiter=",")      
    for row in reader:       
        row_count+=1
        print("Row:", row_count)
        output_list = []

        city = row[0]
        g = geocoder.bing(city + ', Missouri', key=bing_api_key, method='details')
        results = g.json

        if results != None:    
            output_list.append([results['city'] + ", " + str(results['lat']) + ", " + str(results['lng'])])

        with open(output_file, "a", newline='') as out_file:
            writer = csv.writer(out_file, delimiter=',')  
            for item in output_list:
                writer.writerow(item)



