from pymongo import MongoClient
import psycopg2
import csv

# verbinding postgres, psycopg2, sql
connection = psycopg2.connect('dbname=postgres user=postgres password=groep5')
cursor = connection.cursor()

client = MongoClient('mongodb://localhost:27017/')
database = client.huwebshop
collection = database.products
session = database.sesssions
products = collection.find({})
sessions = session.find({})

for item in products:
    print(item)
