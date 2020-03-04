from pymongo import MongoClient
import psycopg2

#postgres
conn = psycopg2.connect(database="voordeelshop", user = "postgres", password = "groep5", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
print("Opened database successfully")

#mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client.huwebshop
col = db.products
ses= db.sessions
products = col.find({})
sessions= ses.find({})

print(products[0])
#for x in products:
#   print(x['brand'],x['properties']['doelgroep'])

def overzetten_products():
    cur.execute('select product_id from products')
    product_id = cur.fetchall()
    print(product_id)
    print(products[0]['_id'])
    i=0
    for x in products:
        if x['_id'] in product_id:
            i+=1
        else:
            productid = x['_id']
            brand= x['brand']
            category = x['category']
            gender = x['gender']
            doelgroep = x['properties']['doelgroep']
            price= x['price']['selling_price']
            price=price/100
            cur.execute("insert into products (product_id, brand, category, gender,doelgroep,price) values (%s,%s,%s,%s,%s,%s)",(productid, brand, category, gender,doelgroep,price))
            i+=1
    conn.commit()
    cur.close()
    conn.close()
    return


overzetten_products()
cur.execute('select product_id from products')
product_id = cur.fetchall()
print(sessions[0])
print(products[0]["_id"])

#for x in products:
#   print(x['brand'])

cur.close()
conn.close()
