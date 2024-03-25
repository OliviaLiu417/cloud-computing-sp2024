from kafka import KafkaConsumer  # consumer of events
import json
consumer = KafkaConsumer(bootstrap_servers="54.202.228.65:30092")

consumer.subscribe(topics=["weather_nashville_topic", "weather_atlanta_topic", "weather_chicago_topic"])

for msg in consumer:
    value = msg.value.decode('utf-8')
    print("value", value)

    # print incoming message as JSON
    data = json.loads(value)
    print("data", data)

consumer.close()
