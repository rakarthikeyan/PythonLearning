
#using client object to get list of IAM users

import boto3

session=boto3.Session(profile_name="root")
client=session.client(service_name="iam")

user_list=client.list_users()["Users"]

for x in user_list:
    print(x["UserName"])

