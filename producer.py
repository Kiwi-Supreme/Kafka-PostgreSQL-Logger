from kafka import KafkaProducer #KafkaProducer is what you use to send messages to a Kafka topic
import json #Kafka works with bytes, not dictionaries or strings directly. We’ll use json to convert (serialize) a Python dictionary to a JSON-formatted string, and then encode it to bytes before sending it to Kafka.

# Set up Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092', #This tells the producer where the Kafka broker is running. localhost means it's on your own machine, and 9092 is the default Kafka port.
    value_serializer=lambda v: json.dumps(v).encode('utf-8') #This tells Kafka how to convert your Python dictionary into JSON bytes. Kafka only sends bytes, so we serialize the data into a JSON string and then encode it.
)

# Simulate user input
user_input = input("Enter something: ")
message = {'user_input': user_input}

# Send to Kafka topic
producer.send('TheRealDB', message)  #Kafka-topic name
producer.flush() #This forces all buffered messages to be sent immediately.
print("Message sent to Kafka.")
