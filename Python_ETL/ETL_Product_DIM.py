import pandas as pd
import mysql.connector
import os


# Read CSV
# Place Your path here
df = pd.read_csv("C:/Users/Product_Dim.csv")

# Convert Date column to YYYY-MM-DD format
#df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Remove Null values
df = df.where(pd.notnull(df), None)

# Connect to MySQL
conn = mysql.connector.connect(
    host="your host",
    user="your username",
    password="your password",
    database="your database"
)

cursor = conn.cursor()

# Insert rows
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO prod_dim (`Product`,`Manufacturing_Price`,`Prod_Key`) "
        "VALUES (%s,%s,%s)",
        tuple(row)
    )

conn.commit()
print("Data inserted successfully")
