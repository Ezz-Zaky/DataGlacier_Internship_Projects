DROP DATABASE IF EXISTS DG_week2;
CREATE DATABASE DG_week2;
USE DG_week2;
DROP TABLE IF EXISTS city;
CREATE TABLE city
(
city VARCHAR(50) NOT NULL PRIMARY KEY,
population INT,
users INT
);
DROP TABLE IF EXISTS customers;
CREATE TABLE customers
(
customer_id INT NOT NULL PRIMARY KEY,
gender VARCHAR(6),
age INT,
income INT
);
DROP TABLE IF EXISTS transactions;
CREATE TABLE transactions
(
transaction_id INT NOT NULL PRIMARY KEY,
customer_id INT ,
payment_mode VARCHAR(4)
);
DROP TABLE IF EXISTS cab_data;
CREATE TABLE cab_data
(
transaction_id INT NOT NULL PRIMARY KEY,
date_of_travel DATE,
company VARCHAR(10),
city VARCHAR(16) ,
km_traveled DECIMAL(4,2),
price_charged DECIMAL(6,2),
cost_of_trip DECIMAL(6,3),
profit DOUBLE,
profit_per_km DECIMAL(7,5)
);



/*Check the profitability of each company while holding all other variables constant*/
SELECT year(date_of_travel),company,AVG(profit_per_km) as profit_per_km
FROM cab_data
GROUP BY year(date_of_travel),company;
SELECT city,company,AVG(profit_per_km) as profit_per_km
FROM cab_data
GROUP BY city,company;
/*Monthly Profit analysis for seasons*/
SELECT month(date_of_travel) as month_,company,SUM(profit) as profit
FROM cab_data
GROUP BY month(date_of_travel),company;
/*Yearly Profit analysis*/
SELECT year(date_of_travel) as year_,company,SUM(profit) as profit
FROM cab_data
GROUP BY year(date_of_travel),company;
SELECT city,company,AVG(profit_per_km) as profit_per_km
FROM cab_data
GROUP BY city,company;
/*Check each company's potential contribution to covid*/
SELECT cab.city,cab.company, SUM(CASE WHEN t.payment_mode='Cash'THEN  1 ELSE 0 END)as cash_transactions
FROM 
transactions t 
JOIN 
cab_data cab ON t.transaction_id=cab.transaction_id
GROUP BY cab.city,cab.company;
/*Market share analysis*/
SELECT a.city,year(a.date_of_travel) as year_,a.company,(COUNT(DISTINCT t.customer_id)/c.users)*100 as market_share
FROM
cab_data a 
JOIN 
transactions t ON a.transaction_id=t.transaction_id
JOIN 
city c ON a.city=c.city
GROUP BY a.city,year(a.date_of_travel),a.company;

/*customer base analysis on gender*/ 
SELECT year(a.date_of_travel) as year_,a.company,cus.gender,COUNT(DISTINCT t.customer_id) as no_of_cutomers
FROM
cab_data a 
JOIN 
transactions t ON a.transaction_id=t.transaction_id
JOIN 
city c ON a.city=c.city
JOIN 
customers cus on t.customer_id=cus.customer_id
GROUP BY year_,a.company,cus.gender;
/*customer base analysis on age*/ 
SELECT a.company,cus.age,COUNT(DISTINCT t.customer_id) as no_of_cutomers
FROM
cab_data a 
JOIN 
transactions t ON a.transaction_id=t.transaction_id
JOIN 
city c ON a.city=c.city
JOIN 
customers cus on t.customer_id=cus.customer_id
GROUP BY a.company,cus.age;
/*customer base analysis on income (normal distribution)*/ 
SELECT year(a.date_of_travel) as year_,a.company,cus.income as customer_income 
FROM
cab_data a 
JOIN 
transactions t ON a.transaction_id=t.transaction_id
JOIN 
city c ON a.city=c.city
JOIN 
customers cus on t.customer_id=cus.customer_id
GROUP by cus.customer_id;

/*Master dataset*/
select * from cab_data join city on cab_data.city=city.city join transactions on cab_data.transaction_id=transactions.transaction_id join customers on customers.customer_id=transactions.customer_id;
select c.city, c.company,count(t.transaction_id) as total_transactions from transactions t join cab_data c on t.transaction_id=c.transaction_id
group by c.city,c.company;