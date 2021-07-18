import boto3

session = boto3.Session(profile_name="root")
iamclient = session.client(service_name="iam")


# for x in range(1,205):
#     username='karthitestUser'+str(x)
#     iamclient.create_user(UserName=username)

# print("user created")
count = 0

paginator = iamclient.get_paginator('list_users')
print("-----------")
for page in paginator.paginate():
    print(page['Users'])
    for user in page['Users']:
        print(user['UserName'])
        count += 1

print("User Count # ", count)
