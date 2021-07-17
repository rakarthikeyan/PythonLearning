# using default session
# no explicit / custom profile name provided to create session
# using default session

import boto3
client=boto3.client(service_name="iam")

user_list=client.list_users()["Users"]

for x in user_list:
    print(x["UserName"])