from pymongo import MongoClient
import psycopg2

# verbinding sql / sycopg2 / postgres / pgadmin, mongodb
connection = psycopg2.connect('dbname=postgres user=postgres password=groep5')
client = MongoClient('mongodb://localhost:27017/')

# defineren variabelen
cursor = connection.cursor()
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
for x in ophalen.find({}, {"_id":1}):
    print(x)
