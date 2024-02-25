from kafka import KafkaConsumer  # consumer of events
import json
import couchdb

couch = couchdb.Server("http://admin:cloudgroup10@localhost:5984/")
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

# acquire the consumer
consumer = KafkaConsumer(bootstrap_servers="172.31.29.51:9092")

# subscribe to topic
consumer.subscribe(topics=["weather_nashville", "weather_atlanta", "weather_chicago"])

for msg in consumer:
    value = msg.value.decode('utf-8')
    print("value", value)

    # print incoming message as JSON
    data = json.loads(value)
    print("data", data)
    db.save(data)

consumer.close()
