# using Client Object & Filters to get list of all running instances

import boto3

session = boto3.Session(profile_name="devops", region_name="us-east-2")
ec2client = session.client(service_name="ec2", region_name="us-east-2")

response = ec2client.describe_instance_status(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        }
    ], IncludeAllInstances=True
)['InstanceStatuses']
# print(response)
for each_item in response:
    print(each_item['InstanceId'], "|", each_item['InstanceState']
          ['Name'], "|", each_item['AvailabilityZone'])
