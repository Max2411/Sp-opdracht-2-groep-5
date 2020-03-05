import psycopg2

#postgres
conn= psycopg2.connect('dbname=postgres user=postgres password=groep5')
#conn = psycopg2.connect(database="voordeelshop", user = "postgres", password = "groep5", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
print("Opened database successfully")
cur.execute("DROP TABLE products ")
#cur.execute("DROP TABLE sessions ")
cur.execute("""create table products
            (product_id varchar PRIMARY KEY,
	        brand varchar,
	        category varchar,
	        gender varchar,
	        doelgroep varchar,
	        price decimal(6,2));""")
#cur.execute("""create table sesions();
#""")






conn.commit()
cur.close()
conn.close()
