#!/usr/local/bin/python3
import boto3
import pprint
import json
jd = json.dump
pp = pprint.PrettyPrinter(indent=1, depth=5)
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
custom_filter = [{
    'Name':'tag:env', 
    'Values': ['pre']}]
response = client.describe_instances(Filters=custom_filter)
for reservations in response['Reservations']:
    for instance in reservations['Instances']:
        print(instance['VpcId'], instance['PrivateIpAddress'], instance['State'])
