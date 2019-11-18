#!/usr/local/bin/python3
import boto3
elbList = boto3.client('elb')
ec2 = boto3.resource('ec2')

bals = elbList.describe_load_balancers()
for elb in bals['LoadBalancerDescriptions']:
    print('ELB DNS Name : ' + elb['DNSName'])
    for ec2Id in elb['Instances']:
        running_instances = \
            ec2.instances.filter(Filters=[{'Name': 'instance-state-name',
                'Values': ['running']},
                {'Name': 'instance-id',
                'Values': [ec2Id['InstanceId']]}])
        for instance in running_instances:
            print("              Instance : " + instance.public_dns_name)