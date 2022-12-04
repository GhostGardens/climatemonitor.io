import sys
import os
import time
import json
import socket
from google.cloud import bigquery
import getreadings
import requests


def is_valid_ipv4_address(addy):
    try:
        socket.inet_aton(addy)
        return True
    except socket.error:
        return False

def create_items(client,bigqueryDatasetLocation,sensorDataset):
    print('Creating Items')
    print('\n1.1 Create Item\n')

    ip = "127.0.0.1"

    # if there are arguments, replace the IP address
    if len(sys.argv) > 1:
        ip = sys.argv[1]

    print(ip)

    # check the IP address; if it's invalid, ignore the rest of the stuff

    if is_valid_ipv4_address(ip):
        readings = requests.get("http://{}:5000/api/v1/temp".format(ip))

        results = json.loads(readings.content)

        query = "insert into {}.{}.sensordata VALUES (DATETIME(\"{}\"),\"{}\",{},{})".format(bigqueryDatasetLocation,sensorDataset,results['asof'],results['hostname'],results['temperature'],results['humidity'])
        print(query)
        try:
            insert = client.query(query)
        except:
            print("Failed text insert w/ {}".format(query))

def run_sensor():

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/pi/bqkey.json'
    bigqueryDatasetLocation = "climatemonitor-io-314313"
    sensorDataset = "climate"
	
    client = bigquery.Client()

    create_items(client,bigqueryDatasetLocation,sensorDataset)

if __name__ == '__main__':
    run_sensor()
