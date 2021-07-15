import boto3
from botocore.translate import _merge_client_retry_config
session=boto3.Session(profile_name="devops",region_name="us-east-2")
resourceobj=session.resource(service_name="ec2")
myec2Instance=resourceobj.Instance('i-0786d1a6592b6a466')
myec2Instance.stop()
myec2Instance.wait_until_stopped()
print("Instance Stopped")
print("Now starting...")
myec2Instance.start()
myec2Instance.wait_until_running()
print(myec2Instance.state())
#print(dir(myec2Instance))