# Import the BOTO3 library
import boto3

# Initiate the client that will be used, in this project, will be "EC2"
ec2 = boto3.client('ec2')

# Create an EC2 instance
response = ec2.run_instances(
    ImageId='ami-06e46074ae430fba6',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=3,
    )

for instance in response['Instances']:
    print(instance['InstanceId'])
