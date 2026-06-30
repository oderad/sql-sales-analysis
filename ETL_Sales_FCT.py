import pandas as pd
import mysql.connector
import os

# Read CSV
# Place your path here
df = pd.read_csv("C:/Users/Sales_Fact.csv")

# Convert Date column to YYYY-MM-DD format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')

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
        "INSERT INTO sales_fct (`Sales_ID`,`Seg_Key`,`Cty_Key`,`Prd_Key`,`Discount_Band`,`Units_Sold`,`Sale_Price`,`Gross_Sales`,`Discounts`,`Sales`,`COGS`,`Profit`,`Date`) "
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        tuple(row)
    )

conn.commit()
print("Data inserted successfully")