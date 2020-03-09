from pymongo import MongoClient
import psycopg2
import csv

# verbinding sql / sycopg2 / postgres / pgadmin, mongodb
connection = psycopg2.connect('dbname=postgres user=postgres password=groep5')
client = MongoClient('mongodb://localhost:27017/')

# defineren variabelen
cursor = connection.cursor()
database = client.huwebshop
# voor onderstaande:.x aanpassen om andere collectie op te halen
ophalen = database.products
session = database.sesssions
products = ophalen.find({})
sessions = session.find({})

# volledige inhoud opvragen
# for item in products:
#     print(item)

# specifieke object(en) uit collection ophalen
mydict = []
for specifiek_object in ophalen.find({}, {"_id":1}):
    formateren = specifiek_object
    mydict.append(formateren)

print(mydict)

# schrijven naar csv bestand
veldnaam = ['_id']
bestandsnaam = 'test.csv'
with open(bestandsnaam, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=veldnaam, lineterminator='\n')
    # writing headers (veldnaam)
    writer.writeheader()
    # writing data rows
    writer.writerows(mydict)
# \copy products FROM ‘cpath\to\csv.csv’ DELIMITER ‘,’ CSV HEADER;