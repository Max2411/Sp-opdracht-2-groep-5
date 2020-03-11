from pymongo import MongoClient
import psycopg2
import csv


def cursor_created(database_name, user, password):
    data = "dbname={} user={} password={}".format(database_name, user, password)
    conn = psycopg2.connect(data)
    cur = conn.cursor()
    return cur


def connect_collection(collection_chosen):  # Connect met een collectie die je kan kiezen bij aanroepen.(procedureel)
    client = MongoClient('mongodb://localhost:27017/')
    database = client.webshop
    collection = database[collection_chosen]
    return collection


def create_collection_list():
    collection_created = connect_collection().find({})
    return collection_created


cursor_created('postgres', 'postgres', 'groep5'), connect_collection(products)


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
