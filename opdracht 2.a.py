import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['huwebshop']
collection = db['products']

def eerste_product():
    print(collection.find_one())

def specifiek_product():
    for product in collection.find():
        if product['name'][0] == 'R':
            print(product)
            break

def gemiddelde_prijs():
    x = []
    y = 0
    for product in collection.find():
        try:
            if product['price']['selling_price'] != 0:
                x.append(product['price']['selling_price'])
        except:
            continue
    for item in x:
        y += item
    lengte = len(x)
    berekening = y / lengte / 100
    print((berekening))
