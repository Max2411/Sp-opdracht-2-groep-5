from pymongo import MongoClient
import psycopg2
c= psycopg2.connect('dbname=postgres user=postgres password=')

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
            if brand=='':
                cur.execute("insert into products (product_id, category, gender,doelgroep,price) values (%s,%s,%s,%s,%s,)",(productid, category, gender, doelgroep, price))
            elif category=='':
                cur.execute("insert into products (product_id, brand, gender,doelgroep,price) values (%s,%s,%s,%s,%s)",(productid, brand, gender, doelgroep, price))
            elif gender=='':
                cur.execute("insert into products (product_id, brand, category,doelgroep,price) values (%s,%s,%s,%s,%s)",(productid, brand, category, doelgroep, price))
            elif doelgroep=='':
                cur.execute( "insert into products (product_id, brand, category, gender,price) values (%s,%s,%s,%s,%s)",(productid, brand, category, gender, price))
            elif price=='':
                cur.execute("insert into products (product_id, brand, category, gender,doelgroep) values (%s,%s,%s,%s,%s)",(productid, brand, category, gender, doelgroep))
            else:
                cur.execute("insert into products (product_id, brand, category, gender,doelgroep,price) values (%s,%s,%s,%s,%s,%s)",(productid, brand, category, gender,doelgroep,price))
            i+=1
    conn.commit()
    cur.close()
    conn.close()
    return



import csv_

with open(prodc, w, newline='')as csvout:
    fieldnames =['id',]
    writer =  csv.DictWriter(csvout,fieldnames=fieldnames)
    writer.writeheader()
    for pro in mongdb.find('id', products["_id"],
                            "catogory"

                           )
