#!/usr/local/bin/python3
import boto3
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
custom_filter = [{
    'Name':'ip-permission.protocol',
    'Values': ['icmp']}]
response = client.describe_security_groups(Filters=custom_filter)
for sg in response['SecurityGroups']:
    for perm in sg['IpPermissions']:
        if perm['IpProtocol'] == 'icmp':
            print('sg['GroupName'])