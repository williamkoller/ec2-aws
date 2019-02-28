import datetime

from var_dump import var_dump

import boto3
from botocore.exceptions import ClientError
client = boto3.client('ec2')

snapshots = client.describe_snapshots(OwnerIds=['self'])

for snapshot in snapshots['Snapshots']:
      a = snapshot['StartTime']
      b = a.date()
      c = datetime.datetime.now().date()
      d = c-b
      try:
        if d.days>15:
          id = snapshot['SnapshotId']
          client.delete_snapshot(SnapshotId=id)
      except (ClientError) as e:
        print ("Unexpected error: %s" % e)
