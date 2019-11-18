#!/usr/local/bin/python3
import boto3
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
custom_filter = [{
    'Name':'tag:env', 
    'Values': ['cola']},
    {'Name': 'tag:Name',
    'Values': ['*']}]
response = client.describe_instances(Filters=custom_filter)

for reservations in response['Reservations']:
    for instance in reservations['Instances']:
        for tags in instance['Tags']:
            if tags['Key'] == 'Name':
                print(tags['Value'], instance['PrivateIpAddress'], instance['InstanceId'], instance['State'])
                print('------------------------------------------------')

