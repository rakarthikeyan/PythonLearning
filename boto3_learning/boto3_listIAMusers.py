# script to list all IAM users

import boto3
import datetime
session=boto3.Session(profile_name="root")
iamclient=session.client(service_name="iam")


response = iamclient.list_users()['Users']
count=0
for each_user in response:
    print(each_user['UserName']," | Created on ",each_user['CreateDate'].strftime("%d/%m/%Y"))
    count+=1
print("Count # ", count)