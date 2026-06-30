import pandas as pd
import mysql.connector
import os

# Read CSV
#Place your designated path here
df = pd.read_csv("C:/Users/Country_Dim.csv")

# Convert Date column to YYYY-MM-DD format
#df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Remove Null values
df = df.where(pd.notnull(df), None)

# Connect to MySQL
conn = mysql.connector.connect(
    host="your host here",
    user="username",
    password="Your Password",
    database="Your Database"
)

cursor = conn.cursor()

# Insert rows
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO country_dim (`Country`,`Coun_Key`) "
        "VALUES (%s,%s)",
        tuple(row)
    )

conn.commit()
print("Data inserted successfully")