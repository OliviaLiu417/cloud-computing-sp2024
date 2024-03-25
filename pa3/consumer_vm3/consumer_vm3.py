print("Logging test run")

from kafka import KafkaConsumer  # consumer of events
import json
import couchdb

print("Beginning couchdb")

couch = couchdb.Server("http://admin:cloudgroup10@couchdb-service:5984")
db = None
retry = 5
while not db and retry: 
    try:
        db = couch['weather_data']
    except: 
        #trying to connect to 'weather_data' table without it existing throws an error, 
        #so we handle error by creating the table. 
        #We only attempt to create the table when accessing a non-existing table throws an error 
        #because if the table already exists then the create operation would throw an error, 
        #so we can't just put create() line above access without a try catch block
        db = couch.create('weather_data')
        retry += 1

print("Acquaring the consumer and subscribing to topics")

# acquire the consumer
consumer = KafkaConsumer(bootstrap_servers="54.202.228.65:30092")

# subscribe to topic
consumer.subscribe(topics=["weather_nashville_topic", "weather_atlanta_topic", "weather_chicago_topic"])

print("Receving messages:")

for msg in consumer:
    value = msg.value.decode('utf-8')
    print("value", value)

    # print incoming message as JSON
    data = json.loads(value)
    print("data", data)
    db.save(data)

consumer.close()
