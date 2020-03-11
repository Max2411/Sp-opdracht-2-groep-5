import csv
from Connections import psycopg_connect
from Connections import mongo_connect

conn,cur=psycopg_connect()

products, sessions, profiles=mongo_connect()


def overzetten_products(filename):  #bron: slack info van de les gestuurd door rik boss
    with open(filename, 'w', newline='') as csvout:
        fieldnames = ['id','brand', 'category', 'gender', 'target_audience','price']
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
                                 'target_audience': doelgroep,
                                 'price': price
                                 })
            except KeyError:
                continue
            c += 1
            if c % 10000 == 0:
                print("{} product records written...".format(c))
            if c % 30000 == 0:      #For testing purpose
                print("Finish test")
                break

    print("Finished creating the product database contents.")
def overzetten_sessions(filename): #bron: slack info van de les gestuurd door rik boss
    with open(filename, 'w', newline='') as csvout:
        fieldnames = ["session_id"]
        writer = csv.DictWriter(csvout, fieldnames=fieldnames)
        writer.writeheader()
        c = 0
        for session in sessions:
            try:
                sessionid = session["_id"]
                writer.writerow({'session_id': sessionid
                                 })
            except KeyError:
                continue
            c += 1
            if c % 10000 == 0:
                print("{} product records written...".format(c))
            if c % 30000 == 0:      #For testing purpose
                print("Finish test")
                break
#overzetten_products('products.csv')
overzetten_sessions('sessions.csv')


