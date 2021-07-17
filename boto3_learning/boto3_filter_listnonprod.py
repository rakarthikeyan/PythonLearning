# filter and list non prod servers (tag with env:dev)

import boto3
session = boto3.Session(profile_name="devops", region_name="us-east-2")
ec2client = session.client(service_name="ec2", region_name="us-east-2")

response = ec2client.describe_instances(
    Filters=[
        {
            'Name': 'tag:env',
            'Values': [
                'dev',
            ]
        },
    ]

)['Reservations']

for each_item in response:
    for x in each_item["Instances"]:
        print(x.get('InstanceId'), "|", x.get("InstanceType"), "|",
              x.get("Architecture"), "|", x.get("PrivateIpAddress"), "|", x["State"]["Name"])
