# Class 01 - Launching EC2 Instances

In this project, we will launch an EC2 instance using boto3.

> **Note**
> Read the [first steps](../FIRST_STEPS.md) to configure your environment.

## Launching an EC2 instance

In order to launch an EC2 instance, we need to create a client with the service `ec2` and then call the method `run_instances` with the parameters that we want.

```python
import boto3

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId='ami-06e46074ae430fba6',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
    )

for instance in response['Instances']:
    print(instance['InstanceId'])
```

This script will launch an EC2 instance with the image `ami-06e46074ae430fba6` and the instance type `t2.micro`. The `MinCount` and `MaxCount` parameters are used to specify the number of instances that we want to launch. In this case, we are launching only one instance.
