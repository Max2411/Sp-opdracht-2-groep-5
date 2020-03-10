import psycopg2

#postgres
conn= psycopg2.connect('dbname=postgres user=postgres password=groep5')
#conn = psycopg2.connect(database="voordeelshop", user = "postgres", password = "groep5", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
print("Opened database successfully")
cur.execute("DROP TABLE IF EXISTS order_table ")
cur.execute("DROP TABLE IF EXISTS products ")
cur.execute("DROP TABLE IF EXISTS sessions ")
cur.execute("DROP TABLE IF EXISTS brand ")
cur.execute("DROP TABLE IF EXISTS profile ")
cur.execute("DROP TABLE IF EXISTS category ")
cur.execute("""create table products
            (product_id varchar PRIMARY KEY,
	        brand varchar,
	        category varchar,
	        gender varchar,
	        doelgroep varchar,
	        price decimal(6,2));""")
cur.execute("""create table sessions
           (session_id varchar PRIMARY KEY           );""")
cur.execute("""CREATE TABLE order_table
           (order_id serial primary key,
           product_id varchar,
           session_id varchar);""")
cur.execute("""create table brand
           (brand_id serial primary key,
           brand varchar unique
           );""")
cur.execute("""create table category
           (category_id varchar PRIMARY KEY,
           category varchar
           );""")
cur.execute("""alter table order_table
            add constraint Prod_id
            foreign key(product_id) references products(product_id);""")

# cur.execute("""create table category
#            (category_id varchar PRIMARY KEY,
#            );""")





print("New database added")

conn.commit()
cur.close()
conn.close()
