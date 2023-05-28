CREATE DATABASE adv_works;

USE ADV_WORKS;

-- CRIAR TABELAS SEM CHAVES ESTRANGEIRAS
CREATE TABLE customers(
		customerKey	int primary KEY NOT NULL,
        prefix	varchar(4),
        firstName	varchar(30) NOT NULL,
        lastName	varchar(30) NOT NULL,
        birthDate	date,
        martialStatus	char,
        gender	char,
        email	varchar(255),
        income	varchar(20),
        totalChild	int,
        educationLevel	varchar(255),
        occupation	varchar(255),
        homeOwner	char
);

CREATE TABLE productCategory(
		productCatId	int PRIMARY KEY NOT NULL,
        categoryName	varchar(50) NOT NULL
);

CREATE TABLE calendar(
	date date primary key NOT NULL
);

CREATE TABLE territory(
		salesTerritoryId	int PRIMARY KEY NOT NULL,
        region	varchar(255) NOT NULL,
        country	varchar(255) NOT NULL,
        continent	varchar(255) NOT NULL
);


-- CRIAR TABELAS COM CHAVE ESTRANGEIRAS

CREATE TABLE productsSubcategory(
		productSubcatId	int PRIMARY KEY NOT NULL,
        subCatName	varchar(255) NOT NULL,
        productCatId	int NOT NULL,
        FOREIGN KEY (productCatId) REFERENCES productCategory(productCatId)
);

CREATE TABLE products(
		productKey	int PRIMARY KEY NOT NULL,
        productSubcatId	int NOT NULL,
        productSKU	varchar(10),
        productName	varchar(255),
        modelName	varchar(255),
        productDesc	varchar(255),
        productColor	varchar(20),
        productSize	varchar(10),
        productStyle	char,
        productCost	float NOT NULL,
        productprice	float NOT NULL,
        FOREIGN KEY (productSubcatId) REFERENCES productsSubcategory(productSubcatId)
);

CREATE TABLE sales(
		orderDate	date NOT NULL,
        stockDate	date NOT NULL,
        orderNumber	varchar(10) PRIMARY KEY NOT NULL,
        productKey	int NOT NULL,
        customerKey	int NOT NULL,
        territoryKey	int NOT NULL,
        orderLineItem	int NOT NULL,
        orderQuantity	int NOT NULL,
        FOREIGN KEY (orderDate) REFERENCES calendar(date),
        FOREIGN KEY (productKey) REFERENCES products(productKey),
        FOREIGN KEY (customerKey) REFERENCES customers(customerKey),
        FOREIGN KEY (territoryKey) REFERENCES territory(salesTerritoryId)
        
);

CREATE TABLE returns(
		returnDate	date NOT NULL,
        territoryKey	int NOT NULL,
        productKey	int NOT NULL,
        returnQuantity	int NOT NULL,
        FOREIGN KEY (returnDate) REFERENCES calendar(date),
        FOREIGN KEY (territoryKey) REFERENCES territory(salesTerritoryId),
        FOREIGN KEY (productKey) REFERENCES products(productKey)
        
);

-- Pesquisas

SELECT * FROM CALENDAR;
SELECT * FROM CUSTOMERS;
SELECT * FROM PRODUCTCATEGORY;
SELECT * FROM PRODUCTS;
SELECT * FROM PRODUCTSSUBCATEGORY;
SELECT * FROM SALES;
SELECT * FROM RETURNS;
SELECT * FROM TERRITORY

-- Querys

-- Quais são os 10 produtos mais vendidos (em quantidade) na categoria "Bicicletas"?
SELECT p.productName, SUM(s.orderQuantity) AS totalQuantity
FROM products AS p
LEFT JOIN productsSubcategory AS ps ON p.productSubcatId = ps.productSubcatId
LEFT JOIN productCategory AS pc ON ps.productCatId = pc.productCatId
LEFT JOIN sales AS s ON p.productKey = s.productKey
WHERE pc.categoryName = 'Bikes'
GROUP BY p.productName
ORDER BY totalQuantity DESC
LIMIT 10;

-- Qual é o cliente que tem o maior número de pedidos realizados?
SELECT c.firstName, c.lastName, COUNT(s.orderNumber) AS totalOrders
FROM customers AS c
LEFT JOIN sales AS s ON c.customerKey = s.customerKey
GROUP BY c.customerKey, c.firstName, c.lastName
ORDER BY totalOrders DESC
LIMIT 1;


-- Em qual mês do ano ocorrem mais vendas (em valor total)?
SELECT EXTRACT(MONTH FROM s.orderDate) AS month, SUM(p.productPrice * s.orderQuantity) AS totalSales
FROM sales AS s
JOIN products AS p ON s.productKey = p.productKey
GROUP BY month
ORDER BY totalSales DESC
LIMIT 1;

-- Quais vendedores tiveram vendas com valor acima da média no último ano fiscal?
SELECT t.region, AVG(s.orderQuantity) AS averageSales
FROM sales AS s
JOIN territory AS t ON s.territoryKey = t.salesTerritoryId
WHERE YEAR(s.orderDate) = 2017
GROUP BY t.region 
ORDER BY averageSales DESC;

-- qual é o top 3 países que mais venderam bicicletas?
SELECT t.country, SUM(s.orderQuantity) AS totalQuantity
FROM territory AS t
JOIN sales AS s ON t.salesTerritoryId = s.territoryKey
JOIN products AS p ON s.productKey = p.productKey
JOIN productsSubcategory AS ps ON p.productSubcatId = ps.productSubcatId
JOIN productCategory AS pc ON ps.productCatId = pc.productCatId
WHERE pc.categoryName = 'Bikes'
GROUP BY t.country
ORDER BY totalQuantity desc
LIMIT 3;












