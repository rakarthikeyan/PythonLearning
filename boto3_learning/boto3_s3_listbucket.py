import boto3

session = boto3.Session(profile_name="devops")
s3client = session.client(service_name="s3")
response = s3client.list_buckets()
bucketlst=[]
print("List of Buckets : \n")
for each_bucket in response['Buckets']:
    print(each_bucket['Name'])
    bucketlst.append(each_bucket['Name'])

# using paginators 
print("\n -- Content of Bucket -- \n")
paginator = s3client.get_paginator('list_objects_v2')
for each_bucket in bucketlst:
    response_iterator = paginator.paginate(Bucket=each_bucket)
    for page in response_iterator:
        for item in page['Contents']:
            print(item['Key'], "|", item['LastModified'].strftime("%d-%m-%Y_%H:%M:%S"))
    

print("-- End --")



