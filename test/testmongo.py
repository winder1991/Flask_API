# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 21:43:11 2022

@author: BlueSpark
"""
import pandas as pd
from pymongo import MongoClient

sec = pd.read_csv('../key.csv')
user = sec['username'].iloc[0]
pw = sec['password'].iloc[0]

connection =  "mongodb+srv://{}:{}@cluster0.pjmu6.mongodb.net/?retryWrites=true&w=majority".format(user, pw)
client = MongoClient(connection)

db = client.ComEnergy
collection_name = db.list_collection_names()