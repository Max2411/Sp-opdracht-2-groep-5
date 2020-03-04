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

def overzetten_products():
    cur.execute('select product_id from products')
    product_id = cur.fetchall()
    print(product_id)
    print(products[0]['_id'])
    i=0
    for x in products:
        productid = products[x]['_id']
        brand= products[x]['brand']
        category = products[x]['category']
        gender = products[x]['gender']
        doelgroep = products[x]['doelgroep']
        values=(productid, brand, category, gender,doelgroep)
        cur.execute("insert into products (product_id, brand, category, gender, doelgroep) values (%s,%s,%s,%s,%s)",values)
        i+=1
    conn.commit()
    cur.close()
    conn.close()
    return
overzetten_products()