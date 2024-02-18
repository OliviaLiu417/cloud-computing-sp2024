import sys
import time
import json
import requests
from kafka import KafkaProducer
from datetime import datetime

# OpenWeatherMap API configuration
API_KEY = "1efe32238e1a430cbbcc25f4c45b9b9e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Kafka configuration
BOOTSTRAP_SERVERS = "35.85.145.90:9092" # vm1

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    acks=1,  # wait for leader to write to the log
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # serialize json messages
)

def fetch_weather_data(city_name):
    """Fetch weather data for a given city from OpenWeatherMap API."""
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def produce_weather_data(city_name):
    """Fetch weather data and produce it to a city-specific Kafka topic."""
    for i in range(5):
        # Fetch weather data
        data = fetch_weather_data(city_name)
        timestamp = datetime.now().isoformat()
        data['timestamp'] = timestamp

        # TODO: Define city-specific Kafka topic
        # kafka_topic = f"weather_data_{city_name.lower().replace(' ', '_')}"
        kafka_topic = f"weather_data_{city_name.lower()}"
        
        # Send data to Kafka
        producer.send(kafka_topic, value=data)
        print(f"Produced weather data for {city_name} to topic {kafka_topic}: {data} \n")
        
        # Sleep for a while before sending the next data
        time.sleep(5)  # Sleep for 10 seconds

if __name__ == "__main__":
    # List of cities to monitor
    cities = ["Nashville", "Atlanta", "Chicago"]

    if len(sys.argv) != 2:
        print("Usage: python3 file_name.py <city_index>")
        print("where <city_index> is:")
        for index, city in enumerate(cities):
            print(f"{index} : {city}")
        sys.exit(1)

    # Get the city index from command line argument
    try:
        city_index = int(sys.argv[1])
        city_name = cities[city_index]
    except (ValueError, IndexError):
        print("Invalid city index. Please provide a valid integer representing a city.")
        sys.exit(1)
    
    produce_weather_data(city_name)
