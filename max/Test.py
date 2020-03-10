import csv
from Connections import psycopg_connect
from Connections import mongo_connect

conn,cur=psycopg_connect()

products, sessions, profiles=mongo_connect()

def overzetten_products(): #bron: slack info van de les gestuurd door rik boss
    with open('products.csv', 'w', newline='') as csvout:
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
