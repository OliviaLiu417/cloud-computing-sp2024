#
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, demonstrate Kafka streaming API to build a consumer.
#

import os   # need this for popen
import time  # for sleep
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
# (you will need to change this to your bootstrap server's IP addr)
consumer = KafkaConsumer(bootstrap_servers="172.31.29.51:9092")

# subscribe to topic
consumer.subscribe(topics=["weather_data_nashville", "weather_data_atlanta", "weather_data_chicago"])

# we keep reading and printing
for msg in consumer:
    # what we get is a record. From this record, we are interested in printing
    # the contents of the value field. We are sure that we get only the
    # utilizations topic because that is the only topic we subscribed to.
    # Otherwise we will need to demultiplex the incoming data according to the
    # topic coming in.
    #
    # convert the value field into string (ASCII)
    #
    # Note that I am not showing code to obtain the incoming data as JSON
    # nor am I showing any code to connect to a backend database sink to
    # dump the incoming data. You will have to do that for the assignment.
   
    value = msg.value.decode('utf-8')
    print("value", value)

    # print incoming message as JSON
    data = json.loads(value)
    print("data", data)
    db.save(data)


# we are done. As such, we are not going to get here as the above loop
# is a forever loop.
consumer.close()
