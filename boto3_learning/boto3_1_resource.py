import boto3

# get list of iam users

mgt_console=boto3.Session(profile_name="root")
iam_console=mgt_console.resource("iam")

print("--- iam ---")

for x in iam_console.users.all():
    print(x.name)

# get list of s3 buckets
print("---- s3 ---")
s3_console=mgt_console.resource("s3")
for x in s3_console.buckets.all():
    print(x.name)

