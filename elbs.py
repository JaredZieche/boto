#!/usr/local/bin/python3
## imported python dependencies ##
import boto3

## resource lists ##
lbas = []

## boto client resource ##
client = boto3.client('elbv2')

## client paginators ##
lb_paginator = client.get_paginator('describe_load_balancers')
tg_paginator = client.get_paginator('describe_target_groups')

## client paginator iterators ##
lb_paginator_iterator = lb_paginator.paginate(LoadBalancerArns=lbas)
tg_paginator_iterator = tg_paginator.paginate(LoadBalancerArn=lbas)

for aws_lb in lb_paginator_iterator:
    for lb_name in aws_lb['LoadBalancers']:
        print("LoadBalancer: " + lb_name['LoadBalancerName'])
        print(" ")
        print("TargetGroups associated with " + lb_name['LoadBalancerName'] + ":")
        print(" ")
        tg_paginator_iterator = tg_paginator.paginate(LoadBalancerArn=lb_name['LoadBalancerArn'])
        for aws_tg in tg_paginator_iterator:
            for tg_name in aws_tg['TargetGroups']:
                print(tg_name['TargetGroupName'])
                print(" ")
                print("TargetGroup Instances:")
                instances = client.describe_target_health(TargetGroupArn=tg_name['TargetGroupArn'])
                for target in instances['TargetHealthDescriptions']:
                    print(target['Target'], target['TargetHealth'])
                print(" ")
            print("----------------------------------------------")