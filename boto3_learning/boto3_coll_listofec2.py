# using filers - get list of running ec2-instances
# display instance id, instance type, architecture, internal IP address

import boto3

session = boto3.Session(profile_name="devops", region_name="us-east-2")
ec2client = session.client(service_name="ec2", region_name="us-east-2")

response = ec2client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
    ]

)['Reservations']


for each_item in response:
    for x in each_item["Instances"]:
        print(x.get('InstanceId'), "|", x.get("InstanceType"), "|",
              x.get("Architecture"), "|", x.get("PrivateIpAddress"))
