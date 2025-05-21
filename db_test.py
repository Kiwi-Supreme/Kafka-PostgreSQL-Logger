#This script: Tries to connect to a PostgreSQL database and Prints a success message if it works,else Prints the error if something goes wrong.

import psycopg2
#psycopg2 is a library that allows your Python code to connect to and interact with PostgreSQL databases

try:
    conn = psycopg2.connect(
        host="127.0.0.1", #Localhost (IPv4). This means the PostgreSQL server is running on your own computer
        port="5432",
        database="KafkaProject", #name of the database
        user="postgres",
        password="Nia-2004" 
    )
    print("Connection successful.")
except Exception as e:
    print(f"Connection failed: {e}")