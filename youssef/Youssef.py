from pymongo import MongoClient
import psycopg2
import csv

# verbinding sql / sycopg2 / postgres / pgadmin, mongodb
connection = psycopg2.connect('dbname=postgres user=postgres password=groep5')
client = MongoClient('mongodb://localhost:27017/')

# defineren variabelen
cursor = connection.cursor()
client = MongoClient('mongodb://localhost:27017/')
database = client.huwebshop
collection = database.products
session = database.sesssions
products = collection.find({})
sessions = session.find({})

# volledige inhoud opvragen
for item in products:
    print(item)
