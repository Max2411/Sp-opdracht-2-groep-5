from pymongo import MongoClient
import psycopg2
import csv

# verbinding sql / sycopg2 / postgres / pgadmin, mongodb
connection = psycopg2.connect('dbname=postgres user=postgres password=groep5')
client = MongoClient('mongodb://localhost:27017/')

# defineren variabelen
# cursor = connection.cursor()
client = MongoClient('mongodb://localhost:27017/')
database = client.huwebshop
# .x aanpassen om andere collection op te halen
ophalen = database.products
session = database.sesssions
products = ophalen.find({})
sessions = session.find({})

# volledige inhoud opvragen
# for item in products:
#     print(item)

# specifieke object(en) uit collection ophalen
# for x in ophalen.find({}, {"_id":1}):
# #     print(x)

# naar csv schrijven
# my data rows as dictionary objects
mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
         {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
         {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
         {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
         {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
         {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]

# field names
fields = ['name', 'branch', 'year', 'cgpa']

# name of csv file
filename = "products.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(mydict)
