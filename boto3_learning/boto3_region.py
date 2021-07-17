
# Code to Iterate through the AWS regions and find status of the ec2 machines

import boto3

mgt_console = boto3.Session(profile_name="devops")
ec2 = mgt_console.client('ec2')
regions = ec2.describe_regions()["Regions"]

for x in regions:
    # print(x['RegionName'])
    ec21 = mgt_console.client('ec2', region_name=x['RegionName'])
    response = ec21.describe_instance_status()['InstanceStatuses']
    if len(response) > 0:
        print("Region:", x['RegionName'])
        for each_instance in response:
            print(each_instance['InstanceId'], '|',
                  each_instance['InstanceState']['Name'])
