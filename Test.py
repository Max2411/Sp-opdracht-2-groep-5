from pymongo import MongoClient
import psycopg2

conn = psycopg2.connect(database="voordeelshop", user = "postgres", password = "groep5", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

#mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client.huwebshop
col = db.products
ses= db.sessions
products = col.find({})
sessions= ses.find({})
#postgres
cur = conn.cursor()


print(products[0])
productid = products[2]['_id']
brand= products[2]['brand']
category = products[2]['category']
gender = products[2]['gender']
#doelgroep = products[1]['doelgroep']
print(sessions[0])
cur.execute("insert into products (product_id, brand, category, gender) values (%s,%s,%s,%s)",(productid, brand, category, gender))
cur.execute('select * from products')
row= cur.fetchall()
print(row)
#for x in products:
#    print(x)
conn.commit()
cur.close()
conn.close()
