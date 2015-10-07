# -*- coding: utf-8 -*-
"""
MIS40750 Assignment 1
Choose a location for a processing plant and port based on inputs from database
renewable.db

Inputs: renewable.db containing two tables
        location: long, lat, production
        ports: long, lat

Author: Micheál Boland
Student Number: 15204343
Date: 3/10/2015 

"""

#----------------------------------------------------------------------------------------
# Function to calculate distance between two point from their latitudes and longitudes
# This function uses the Haversines formula
# Inputs: lat1, lon1: latitudes and longitudes of location 1
#         lat2, lon2: latitude and longitude of location 2
# Output: dist_calc: distance between the two points

def dist_calc(lat1,lon1,lat2,lon2):
    # Splitting Havesine formula into two parts for conciseness.    
    h = ((math.sin((math.radians(lat2)-math.radians(lat1))/2))**2) + \
    math.cos(math.radians(lat1))*math.cos(math.radians(lat2))* \
    ((math.sin((math.radians(lon2)-math.radians(lon1))/2))**2)   
        
    # h multiplied by radius of Earth which is 6371 km
    return 2*6371*math.asin(math.sqrt(h))
    
#----------------------------------------------------------------------------------------

# Importing relevant modules
import sqlite3
import numpy as np
import math  

# Read in values of location from location table on renewable.db
conn = sqlite3.connect("renewable.db")
curs = conn.cursor()
loc_lat = curs.execute("select * from location")

for i in loc_lat:
    print i

# Distance between these points ~1.05 km
lt1 = 53.355
ln1 = -6.448
lt2 = 53.356
ln2 = -6.433

print dist_calc(lt1,ln1,lt2,ln2)
    