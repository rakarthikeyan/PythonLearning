import json
import boto3

mgt_console = boto3.Session(profile_name="devops")
ec2 = mgt_console.client('ec2')
regions = ec2.describe_regions()["Regions"]

myMessage=""
for x in regions:
    # print(x['RegionName'])
    ec21 = mgt_console.client('ec2', region_name=x['RegionName'])
    response = ec21.describe_instance_status()['InstanceStatuses']
    
    if len(response) > 0:
        myMessage="Region: "+ x['RegionName'] + "\n"
        #print("Region:", x['RegionName'])
        for each_instance in response:
            myMessage=myMessage + each_instance['InstanceId'] + '|' + each_instance['InstanceState']['Name'] + "\n"
            #print(each_instance['InstanceId'], '|',
            #      each_instance['InstanceState']['Name'])

print(myMessage)