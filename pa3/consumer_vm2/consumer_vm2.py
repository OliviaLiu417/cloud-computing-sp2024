from kafka import KafkaConsumer  # consumer of events
import json
consumer = KafkaConsumer(bootstrap_servers="kafka:9092")

consumer.subscribe(topics=["weather_nashville", "weather_atlanta", "weather_chicago"])

for msg in consumer:
    value = msg.value.decode('utf-8')
    print("value", value)

    # print incoming message as JSON
    data = json.loads(value)
    print("data", data)

consumer.close()
