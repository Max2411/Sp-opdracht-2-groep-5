from pymongo import MongoClient
import psycopg2
import csv
conn= psycopg2.connect('dbname=postgres user=postgres password=groep5')

#postgres
# conn = psycopg2.connect(database="voordeelshop", user = "postgres", password = "groep5", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
print("Opened database successfully")

#mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client.huwebshop
col = db.products
ses= db.sessions
products = col.find({})
sessions= ses.find({})


def overzetten_products(): #bron: slack info van de les gestuurd door rik boss
    with open('test.csv', 'w', newline='') as csvout:
        fieldnames = ['id','brand', 'category', 'gender', 'doelgroep','price']
        writer = csv.DictWriter(csvout, fieldnames=fieldnames)
        writer.writeheader()
        c = 0
        for product in products:
            try:
                productid = product['_id']
                brand = product['brand']
                category = product['category']
                gender = product['gender']
                doelgroep = product['properties']['doelgroep']
                price = product['price']['selling_price']
                price = price / 100
                writer.writerow({'id': productid,
                                 'brand':brand,
                                 'category': category,
                                 'gender':gender,
                                 'doelgroep': doelgroep,
                                 'price': price
                                 })
            except KeyError:
                continue
            c += 1
            if c % 10000 == 0:
                print("{} product records written...".format(c))
    print("Finished creating the product database contents.")
overzetten_products()
# \copy products FROM ‘cpath\to\csv.csv’ DELIMITER ‘,’ CSV HEADER;
