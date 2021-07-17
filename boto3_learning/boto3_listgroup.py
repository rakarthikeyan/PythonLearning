# script to list the groups & their creation time

import boto3
import datetime
import botocore
session=boto3.Session(profile_name="root")
iamclient=session.client(service_name="iam")
response = iamclient.list_groups()['Groups']
for each_group in response:
    print(each_group['GroupName'], '| Created on ', each_group['CreateDate'].strftime("%d/%m/%Y"))