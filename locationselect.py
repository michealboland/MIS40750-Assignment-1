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

# Importing sqlite3 module
import sqlite3

# Read in values of location from location table on renewable.db
conn = sqlite3.connect("renewable.db")
curs = conn.cursor()
lat = curs.execute("select lat from location")

print lat
    