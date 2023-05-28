import mysql.connector
import numpy as np
import pandas as pd

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "admin",
    "database": "adv_works",
}  # Configuração do Banco de Dados

try:
    conn = mysql.connector.connect(**db_config)  # Iniciar conexão com o Banco

    cursor = conn.cursor()
    # 1 ----------------------------------------------------------------------------------------------------------------
    path_customers = r"C:\Users\arleg\OneDrive\Documentos\DesafioDadosSD\Desafio_1\archive\arquivo_tratado\AdventureWorks_Customers_tratado.csv"
    # Inserts para a table de *customers*

    customers = pd.read_csv(path_customers, encoding="latin1")
    customers = customers.replace({np.nan: None})
    for customer in customers.itertuples(index=False):
        print(customer)
        query_customer = "INSERT INTO customers (customerKey, prefix, firstName, lastName, birthDate, martialStatus, gender, email, income, totalChild, educationLevel, occupation, homeOwner) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query_customer, customer)
        print("Inserção de dados da tabela Customers")
        print(customer)

    print("Dados da tabela Customers registrados com Sucesso!")

    # 2 -----------------------------------------------------------------------------------------------------------------------
    path_productCategory = r"C:\Users\arleg\OneDrive\Documentos\DesafioDadosSD\Desafio_1\archive\produtos\AdventureWorks_Product_Categories.csv"
    # Inserts para a table de *productCategory*
    productCategory = pd.read_csv(path_productCategory, encoding="latin1")
    productCategory = productCategory.replace({np.nan: None})
    for category in productCategory.itertuples(index=False):
        query_productCategory = (
            "INSERT INTO productCategory (productCatId, categoryName) VALUES (%s, %s);"
        )
        cursor.execute(query_productCategory, category)
        print("Inserção de dados da tabela productCategory")
        print(category)

    print("Dados da tabela productCategory registrados com Sucesso!")

    # 3 ----------------------------------------------------------------------------------------------------------------------------------
    path_calendar = r"C:\Users\arleg\OneDrive\Documentos\DesafioDadosSD\Desafio_1\archive\arquivo_tratado\AdventureWorks_Calendar_tratado.csv"
    # Inserts para table de *calendar*
    calendar = pd.read_csv(path_calendar, encoding="latin1")
    calendar = calendar.replace({np.nan: None})
    for date in calendar.itertuples(index=False):
        query_calendar = "INSERT INTO calendar (date) VALUES (%s);"

        cursor.execute(query_calendar, date)
        print("Inserção de dados da tabela calendar")
        print(date)

    print("Dados da tabela calendar registrados com Sucesso!")

    # 4 ------------------------------------------------------------------------------------------------------------------------------------
    path_territory = r"C:\Users\arleg\OneDrive\Documentos\DesafioDadosSD\Desafio_1\archive\AdventureWorks_Territories.csv"
    # Inserts para table *territory*
    territories = pd.read_csv(path_territory, encoding="latin1")
    territories = territories.replace({np.nan: None})
    for territory in territories.itertuples(index=False):
        query_territory = "INSERT INTO territory (salesTerritoryId, region, country, continent) VALUES (%s, %s, %s, %s);"

        cursor.execute(query_territory, territory)
        print("Inserção de dados da tabela territory")
        print(territory)

    print("Dados da tabela territory registrados com Sucesso!")

    # 5 ----------------------------------------------------------------------------------------------------------------------------------
    path_productsSubcategory = r"C:\Users\arleg\OneDrive\Documentos\DesafioDadosSD\Desafio_1\archive\produtos\AdventureWorks_Product_Subcategories.csv"
    # Inserts para table *productsSubcategory*
    productsSubcategories = pd.read_csv(path_productsSubcategory, encoding="latin1")
    productsSubcategories = productsSubcategories.replace({np.nan: None})
    for productsSubcategory in productsSubcategories.itertuples(index=False):
        query_productsSubcategory = "INSERT INTO productsSubcategory (productSubcatId, subCatName, productCatId) VALUES (%s, %s, %s);"

        cursor.execute(query_productsSubcategory, productsSubcategory)
        print("Inserção de dados da tabela productsSubcategory")
        print(productsSubcategory)

    print("Dados da tabela productsSubcategory registrados com Sucesso!")

    # 6 --------------------------------------------------------------------------------------------------------------------------------------
    path_products = r"C:\Users\arleg\OneDrive\Documentos\DesafioDadosSD\Desafio_1\archive\produtos\AdventureWorks_Products.csv"
    # Inserts para table *products*
    products = pd.read_csv(path_products, encoding="latin1")
    products = products.replace({np.nan: None})
    for product in products.itertuples(index=False):
        query_products = "INSERT INTO products (productKey, productSubcatId, productSKU, productName, modelName, productDesc, productColor, productSize, productStyle, productCost, productprice) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        cursor.execute(query_products, product)
        print("Inserção de dados da tabela products")
        print(product)

    print("Dados da tabela products registrados com Sucesso!")

    # 7 --------------------------------------------------------------------------------------------------------------------------------------
    path_sales = r"C:\Users\arleg\OneDrive\Documentos\DesafioDadosSD\Desafio_1\archive\arquivo_tratado\AdventureWorks_Sales_2015_tratado.csv"
    # Inserts para table *sales*
    sales = pd.read_csv(path_sales, encoding="latin1")
    sales = sales.replace({np.nan: None})
    for sale in sales.itertuples(index=False):
        query_sales = "INSERT INTO sales (orderDate, stockDate, orderNumber, productKey, customerKey, territoryKey, orderLineItem, orderQuantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

        cursor.execute(query_sales, sale)
        print("Inserção de dados da tabela sales 2015")
        print(sale)

    print("Dados da tabela sales registrados com Sucesso!")
    # -------------------------------------------------------------------------------------------------------------------------------------------
    path_sales = r"C:\Users\arleg\OneDrive\Documentos\DesafioDadosSD\Desafio_1\archive\arquivo_tratado\AdventureWorks_Sales_2016_tratado.csv"
    # Inserts para table *sales*
    sales = pd.read_csv(path_sales, encoding="latin1")
    sales = sales.replace({np.nan: None})
    for sale in sales.itertuples(index=False):
        query_sales = "INSERT INTO sales (orderDate, stockDate, orderNumber, productKey, customerKey, territoryKey, orderLineItem, orderQuantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

        cursor.execute(query_sales, sale)
        print("Inserção de dados da tabela sales 2016")
        print(sale)

    print("Dados da tabela sales registrados com Sucesso!")
    # -------------------------------------------------------------------------------------------------------------------------------------------
    path_sales = r"C:\Users\arleg\OneDrive\Documentos\DesafioDadosSD\Desafio_1\archive\arquivo_tratado\AdventureWorks_Sales_2017_tratado.csv"
    # Inserts para table *sales*
    sales = pd.read_csv(path_sales, encoding="latin1")
    sales = sales.replace({np.nan: None})
    for sale in sales.itertuples(index=False):
        query_sales = "INSERT INTO sales (orderDate, stockDate, orderNumber, productKey, customerKey, territoryKey, orderLineItem, orderQuantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

        cursor.execute(query_sales, sale)
        print("Inserção de dados da tabela sales 2017")
        print(sale)

    print("Dados da tabela sales registrados com Sucesso!")

    # 8 -------------------------------------------------------------------------------------------------------------------------------------------
    path_returns = r"C:\Users\arleg\OneDrive\Documentos\DesafioDadosSD\Desafio_1\archive\arquivo_tratado\AdventureWorks_Returns_tratado.csv"
    # Inserts para table *returns*
    returns = pd.read_csv(path_returns, encoding="latin1")
    returns = returns.replace({np.nan: None})
    for ret in returns.itertuples(index=False):
        query_returns = "INSERT INTO returns (returnDate, territoryKey, productKey, returnQuantity) VALUES (%s, %s, %s, %s);"

        cursor.execute(query_returns, ret)
        print("Inserção de dados da tabela returns")
        print(ret)

    print("Dados da tabela returns registrados com Sucesso!")

    # Commitando alterações
    conn.commit()

except mysql.connector.Error as error:
    print(f"Erro ao inserir dados no banco de dados: {error}")


finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
