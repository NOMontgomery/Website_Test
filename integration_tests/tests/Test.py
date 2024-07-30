# Depencies to install

# pip install pandas
# pip install pypyodbc
# pip install pytest

import pytest
import pypyodbc
import pandas as pd
from datetime import datetime

# list credentils
# Trusted connection = no 
# server = 'homepro.database.windows.net'
# database = 'main'
# username = 'HomeProUser'
# password = 'qwerty_123'

connection = pypyodbc.Connection(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=homepro.database.windows.net;DATABASE=main; UID=HomeProUser; '
    'PWD=qwerty_123;Trusted_Connection=NO')
print(f'Connect to the Database')
# cursor.execute("SELECT * FROM HomePro.Customers")
cursor = connection.cursor()


def test_query():
    query = """ SELECT SUM(Estimation) as 'sum of qoutes'
    FROM HomePro.Customers a
    JOIN HomePro.Quotes b
    ON a.CustomerId = b.CustomerId
    join HomePro.Schedules c
    on b.CustomerId = c.CustomerId
    where DateNeeded < '2015-01-01'
    """
    df = pd.read_sql(query, connection)

    # assert pd.FirstName
    print(f'{df}')
    cursor.close()
    connection.close()


def test_new_query():
    SQL_Query_2 = """select * 
    from HomePro.Customers a
    JOIN HomePro.Schedules b
    on a.CustomerId = b.CustomerId
    JOIN HomePro.Quotes c
    on b.CustomerId = c.CustomerId
    where JobType like 'Remodeling' and Estimation < 5000 AND a.Age < 70"""
    df = pd.read_sql(SQL_Query_2, connection)
    print(f'{df}')
    cursor.close()
    connection.close()
