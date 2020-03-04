# Sp-opdracht-2

querycode: 

create table products(
	product_id varchar(255) unique NOT NULL,
	brand varchar(255),
	category varchar(255),
	gender varchar(255),
	doelgroep varchar(255),
	price decimal(6,2)
);