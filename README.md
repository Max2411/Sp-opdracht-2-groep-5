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

Voor de tabel van de products hebben wij gekozen om de volgende data over te zetten:
1. product id om dat deze uniek is waardoor je producten kan onderscheiden.
2. brand zodat je producten van het zelfde merk kan aanraaden die er op lijken.
3. categorie, want producten die onder de zelfde catogorie vallen kunnen een connectie hebben.
4. gender, want mannen willen bijvoorbeeld andere verzorgings middelen dan vrouwen.
5. doelgroepen, want bijvoorbeeld kinderen hebben andere middelen nodig dan mannen.
6. prijs, om de prijzen met elkaar te kunnen vergelijken.