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

# Importing relevant modules
import sqlite3
import math  

#----------------------------------------------------------------------------------------
# Function to calculate distance between two point from their latitudes and longitudes
# This function uses the Haversines formula
# Inputs: lat1, lon1: latitudes and longitudes of location 1
#         lat2, lon2: latitude and longitude of location 2
# Output: dist_calc: distance between the two points

def dist_calc(lon1,lat1,lon2,lat2):
    # Splitting Havesine formula into two parts for neatness    
    h = ((math.sin((math.radians(lat2)-math.radians(lat1))/2))**2) + \
    math.cos(math.radians(lat1))*math.cos(math.radians(lat2))* \
    ((math.sin((math.radians(lon2)-math.radians(lon1))/2))**2)   
        
    # h multiplied by radius of Earth which is 6371 km
    return 2*6371*math.asin(math.sqrt(h))
    
#----------------------------------------------------------------------------------------

# Establishing connection to database using sqlite3
conn = sqlite3.connect("renewable.db")

# Creation of cursor objects
c1 = conn.cursor()
c2 = conn.cursor()

# Creation of an empty dictionary
dictloc = {}
prodsum = 0

# The overall production volume is needed. This only needs to be calculated once
c1.execute("select production from location")
for prod in c1:
    prodsum += prod[0]

# First cursor will execute select command from location table
c1.execute("select long,lat from location")
for loc1 in c1:
    # Here cost is the product of production volume times distance travelled
    cost = 0
    
    # The cost to each location from all others is calculated
    c2.execute("select long,lat,production from location")
    for loc2 in c2:
        cost += dist_calc(loc1[0],loc1[1],loc2[0],loc2[1]) * loc2[2]
    
    # Calculate cost of moving all produce from each location to each port
    c2.execute("select long,lat from ports")
    for por in c2:
        # Dictionary key is a string referencing the location and port. Value is total cost
        # Total Cost = (Cost to each location from all others)+(Cost of moving from location to each port)
        dictloc["Location at Lat: %f Long: %f with Port at Lat: %f Long: %f" % (loc1[0],loc1[1],por[0],por[1])] = \
        cost + (dist_calc(loc1[0],loc1[1],por[0],por[1]) * prodsum)    

# Final step is to retrieve the key in the dictionary for which the value is lowest
result = min(dictloc.items(), key=lambda x: x[1])

# Result printed to screen
print "%s is the most cost effective solution with a total cost of %f tonnes.km" %(result[0],result[1])