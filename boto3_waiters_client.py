import boto3

session=boto3.Session(profile_name="devops")
ec2client=session.client("ec2",region_name='us-east-2')
ec2client.start_instances(InstanceIds=['i-0786d1a6592b6a466'])
waiter=ec2client.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-0786d1a6592b6a466'])
print("Now your ec2 instace is up and running")
response = ec2client.describe_instance_status(
    InstanceIds=[
        'i-0786d1a6592b6a466',
    ],
)
print(response['InstanceStatuses'][0]['InstanceState']['Name'])