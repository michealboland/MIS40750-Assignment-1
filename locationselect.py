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

def dist_compare(lt,ln,cur):
    for j in cur:
        print lt
        print ln
        print j



# Importing relevant modules
import sqlite3
import numpy as np
import math  

# Read in values of location from location table on renewable.db
conn = sqlite3.connect("renewable.db")
c_loc1 = conn.cursor()
c_loc2 = conn.cursor()
c_por = conn.cursor()
c_loc1.execute("select * from location")
l_loc = {}
loc_num = 1

for i in c_loc1:
    
    cost = 0
    prod_sum = 0
    port_num = 1
    
    c_loc2.execute("select * from location")
    for j in c_loc2:
        # The total cost per tonne per km to each location from all other locations is calculated        
        cost += dist_calc(i[0],i[1],j[0],j[1])*j[2]
        prod_sum += j[2]
        
    print "Location: %d %f %f" % (loc_num,cost,prod_sum)
    
    loc_num += 1
    
#    c_por.execute("select * from ports")
#    for k in c_por:
#        l_loc["%d %d" % (loc_num,port_num)] = cost + (dist_calc(i[0],i[1],k[0],k[1])*prod_sum)    
#        port_num += 1
#        
#    loc_num += 1
    

    
    