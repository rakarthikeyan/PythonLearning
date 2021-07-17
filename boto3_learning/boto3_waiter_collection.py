# implement boto3 waiters and collections to start non prod (env:dev) servers

import boto3

session = boto3.Session(profile_name="devops", region_name="us-east-2")
ec2client = session.client(service_name="ec2", region_name="us-east-2")


def filterDevServers():
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

    return response


listDevServers = []

response = filterDevServers()

for each_item in response:
    for x in each_item["Instances"]:
        listDevServers.append(x.get('InstanceId'))


print("Trying to start Dev Instances")
ec2client.start_instances(InstanceIds=listDevServers)
waiter = ec2client.get_waiter('instance_running')
waiter.wait(InstanceIds=listDevServers)
print("The Dev Servers are now Up & Running...")

response = filterDevServers()

for each_item in response:
    for x in each_item["Instances"]:
        print(x.get('InstanceId'), "|", x.get("InstanceType"), "|",
              x.get("Architecture"), "|", x.get("PrivateIpAddress"), "|", x["State"]["Name"])
