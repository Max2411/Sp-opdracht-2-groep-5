from Connections import psycopg_connect
conn, cur=psycopg_connect()

print("Opened database successfully")
cur.execute("DROP TABLE IF EXISTS order_table ")
cur.execute("DROP TABLE IF EXISTS brand ")
cur.execute("DROP TABLE IF EXISTS category ")


cur.execute("DROP TABLE IF EXISTS sessions ")
cur.execute("DROP TABLE IF EXISTS profile ")
cur.execute("DROP TABLE IF EXISTS products ")

cur.execute("""create table products
            (product_id varchar PRIMARY KEY,
	        brand varchar,
	        category varchar,
	        sub_category varchar,
	        sub_sub_category varchar,
	        gender varchar,
	        target_audience varchar, # doelgroep veranderen naar target audience
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
           (category_id serial PRIMARY KEY,
           sub_category_id serial
           category varchar
           );""")
cur.execute("""create table sub_category
           (sub_category_id serial PRIMARY KEY,
           category_id serial,
           sub_category varchar
           );""")
cur.execute("""create table sub_sub_category
           (sub_sub_category_id serial PRIMARY KEY,
           sub_category_id serial,
           sub_sub_category varchar
           );""")

cur.execute("""alter table category
            add constraint cat_id
            foreign key(category_id) references products(category);""")
cur.execute("""alter table sub_category
            add constraint subcat_id
            foreign key(sub_category_id) references category(sub_category_id);""")
cur.execute("""alter table sub_category
            add constraint subcat_id2
            foreign key(sub_category_id) references products(sub_category);""")

cur.execute("""alter table sub_sub_category
            add constraint subsubcat_id
            foreign key(sub_sub_category_id) references sub_category(sub_sub_category_id);""")

cur.execute("""alter table sub_sub_category
            add constraint subsubcat_id2
            foreign key(sub_sub_category_id) references products(sub_sub_category);""")

cur.execute("""alter table order_table
            add constraint Prod_id
            foreign key(product_id) references products(product_id);""")
cur.execute("""alter table order_table
            add constraint Ses_id
            foreign key(session_id) references sessions(session_id);""")
cur.execute("""alter table brand
            add constraint brand_id
            foreign key(brand_id) references products(brand);""")



# cur.execute("""create table category
#            (category_id varchar PRIMARY KEY,
#            );""")


print("New database added")

conn.commit()
cur.close()
conn.close()
