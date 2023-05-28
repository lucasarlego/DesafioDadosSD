import mysql.connector
import pandas as pd

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "admin",
    "database": "adv_works",
}

conn = mysql.connector.connect(**db_config)

# 1 ---------------------------------------------------------------------------------------------------------
query_products = """SELECT p.productName, SUM(s.orderQuantity) AS totalQuantity
FROM products AS p
LEFT JOIN productsSubcategory AS ps ON p.productSubcatId = ps.productSubcatId
LEFT JOIN productCategory AS pc ON ps.productCatId = pc.productCatId
LEFT JOIN sales AS s ON p.productKey = s.productKey
WHERE pc.categoryName = 'Bikes'
GROUP BY p.productName
ORDER BY totalQuantity DESC
LIMIT 10;"""
df_products = pd.read_sql(query_products, conn)
csv_products = r"../DesafioDadosSD\Desafio_1\Query\products.csv"
print("Os resultados foram salvos!")

# 2 -------------------------------------------------------------------------------------------------------------
query_bestcustomer = """SELECT c.firstName, c.lastName, COUNT(s.orderNumber) AS totalOrders
FROM customers AS c
LEFT JOIN sales AS s ON c.customerKey = s.customerKey
GROUP BY c.customerKey, c.firstName, c.lastName
ORDER BY totalOrders DESC
LIMIT 1;"""
df_bestcustomer = pd.read_sql(query_bestcustomer, conn)
csv_bestcustomer = r"../DesafioDadosSD\Desafio_1\Query\bescustomer.csv"
print("Os resultados foram salvos!")

# 3 ---------------------------------------------------------------------------------------------------------------------------
query_totalvalue = """SELECT EXTRACT(MONTH FROM s.orderDate) AS month, SUM(p.productPrice * s.orderQuantity) AS totalSales
FROM sales AS s
JOIN products AS p ON s.productKey = p.productKey
GROUP BY month
ORDER BY totalSales DESC
LIMIT 1;"""
df_totalvalue = pd.read_sql(query_totalvalue, conn)
csv_totalvalue = r"../DesafioDadosSD\Desafio_1\Query\totalvalue.csv"
print("Os resultados foram salvos!")

# 4 -------------------------------------------------------------------------------------------------------------------------------
query_sales = """SELECT t.region, AVG(s.orderQuantity) AS averageSales
FROM sales AS s
JOIN territory AS t ON s.territoryKey = t.salesTerritoryId
WHERE YEAR(s.orderDate) = 2017
GROUP BY t.region
ORDER BY averageSales DESC;"""
df_sales = pd.read_sql(query_sales, conn)
csv_sales = r"../DesafioDadosSD\Desafio_1\Query\sales.csv"
print("Os resultados foram salvos!")

# 5 ----------------------------------------------------------------------------------------------------------------------------------
query_top3 = """SELECT t.country, SUM(s.orderQuantity) AS totalQuantity
FROM territory AS t
JOIN sales AS s ON t.salesTerritoryId = s.territoryKey
JOIN products AS p ON s.productKey = p.productKey
JOIN productsSubcategory AS ps ON p.productSubcatId = ps.productSubcatId
JOIN productCategory AS pc ON ps.productCatId = pc.productCatId
WHERE pc.categoryName = 'Bikes'
GROUP BY t.country
ORDER BY totalQuantity desc
LIMIT 3;"""
df_top3 = pd.read_sql(query_top3, conn)
csv_top3 = r"../DesafioDadosSD\Desafio_1\Query\top3.csv"
print("Os resultados foram salvos!")

# Salvando os CSV
df_products.to_csv(csv_products, index=False)
df_bestcustomer.to_csv(csv_bestcustomer, index=False)
df_totalvalue.to_csv(csv_totalvalue, index=False)
df_sales.to_csv(csv_sales, index=False)
df_top3.to_csv(csv_top3, index=False)

conn.close()
