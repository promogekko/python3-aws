#! /usr/bin/python3

import boto3

#----------------------------------------------------------------
#create une ressource S3
s3 = boto3.resource('s3')

#print(type(s3))

# list des buckets
for bucket in s3.buckets.all():
   print(bucket.name)

# creer un S3 client pour creer un bucket
s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket='192.134.56.78-mybucket')

# ajouter une image
data = open('test.jpg', 'rb')
s3.Bucket('192.134.56.78-mybucket').put_object(Key="test.jpg",Body=data)

#------------------------------------------------------------------------------
sqs= boto3.resource('sqs')
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

print(queue.url)
print(queue.attributes.get('DelaySeconds'))

#------------------------------------------------------------------------------
ec2_client = boto3.client('ec2')
response = ec2_client.describe_instances()
#print(response)

#ec2 = boto3.resource('ec2')
#ec2.create_instances(ImageId='ami-4fffc834', MinCount=1, MaxCount=1)
#ec2.create_instances(ImageId='ami-4fffc834',
#                    InstanceType='t2.micro',
#                    KeyName='pcspecialist',
#                    MinCount=1, MaxCount=1
#                    )

