#!/usr/local/bin/python3
import boto3
import pprint
import json
import csv
jd = json.dump
pp = pprint.PrettyPrinter(indent=1, depth=5)
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
custom_filter = [{
    'Name':'tag:vpc', 
    'Values': ['*']}]
response = client.describe_volumes(Filters=custom_filter)
for volumes in response['Volumes']:
    for tag in volumes['Tags']:
        for attachments in volumes['Attachments']:
            if tag['Key'] == 'vpc':
                print(tag['Value'], volumes['VolumeId'], volumes['CreateTime'], volumes['State'], attachments['State'], volumes['Size'])