from kafka import KafkaConsumer #This lets your script connect to a Kafka topic and receive messages.
import json
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="KafkaProject",
    user="postgres",
    password="Nia-2004"
)

cur = conn.cursor() #This creates a cursor object which is used to execute SQL queries on the database.

# Connect to Kafka topic
consumer = KafkaConsumer(
    'TheRealDB',  #Kafka-topic name
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Consume and store in DB
for message in consumer: #infinite loop
    data = message.value
    user_input = data['user_input']
    cur.execute("INSERT INTO messages (user_input) VALUES (%s)", (user_input,)) #Executes an SQL INSERT statement to store the user input into your messages table
    conn.commit() #Saves the change permanently in the database.
    print(f"Stored in DB: {user_input}")
