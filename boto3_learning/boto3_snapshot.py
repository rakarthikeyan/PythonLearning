# boto3 script to create snapshot of the ebs volumes on us-east-2
# copy the snapshot to us-east-1

import boto3
import datetime

# get list of ebs volume with status = attached

session = boto3.Session(profile_name="devops")
ec2client = session.client(service_name="ec2", region_name="us-east-2")
ec2client_dest = session.client(service_name="ec2", region_name="us-east-1")

response = ec2client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.status',
            'Values': [
                'attached',
            ]
        },
    ]
)['Volumes']

listvol = []
listsnap = []
for each_item in response:
    for vol in each_item['Attachments']:
        listvol.append(vol['VolumeId'])

# print()

for volID in listvol:
    response = ec2client.create_snapshot(
        Description='Backup SnapShot -' +
        datetime.datetime.now().strftime('%d_%m_%Y_%H:%M:%S'),
        VolumeId=volID)
    listsnap.append(response['SnapshotId'])

print("Creating Snapshot....")
waiter = ec2client.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=listsnap)
print("Snapshot Operation Completed Succesfully")
print("Begin transfer to us-east-1..")
lstdestsnapID = []
for each_snap in listsnap:
    response = ec2client_dest.copy_snapshot(
        Description='Copied from us-east-2' +
        datetime.datetime.now().strftime('%d_%m_%Y_%H:%M:%S'),
        SourceRegion='us-east-2',
        SourceSnapshotId=each_snap,
    )
    lstdestsnapID.append(response['SnapshotId'])


waiter = ec2client_dest.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=lstdestsnapID)
print("Backup to us-east-1 : Completed")
