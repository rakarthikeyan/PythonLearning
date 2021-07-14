import boto3
import time
session=boto3.Session(profile_name="devops",region_name='us-east-2')
client=session.client(service_name="ec2",region_name='us-east-2')

#Start a ec2 instance 

# response = client.start_instances(
#     InstanceIds=[
#         'i-0786d1a6592b6a466',
#     ]
# )

#Get details of the ec2 instance

response = client.describe_instances(
    
    InstanceIds=[
        'i-0786d1a6592b6a466',
    ],
    
)["Reservations"][0]['Instances'][0]

print(response)

for key,value in response.items():
    print(key,":",value)

# print("PublicIpAddress : ", response.get('PublicIpAddress'))
# print("PublicDnsName : ", response.get('PublicDnsName'))
# print("State : ", response.get('State'))


#Stop a ec2 instance 

# response = client.stop_instances(
#     InstanceIds=[
#         'i-0786d1a6592b6a466',
#     ]
# )


