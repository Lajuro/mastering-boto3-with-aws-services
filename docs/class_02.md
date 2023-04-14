# Operations on EC2 (Start, Stop and Terminate)

In this project, we will start, stop and terminate an EC2 instance using boto3.

> **Note**
>
> Read the [first steps](../FIRST_STEPS.md) to configure your environment.

All the information about `EC2 for BOTO3` you can find [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html).

## Operations on EC2

In the class was used a more common approach using functions, but instead, we will use a class to encapsulate the operations.

```python
import boto3


INSTANCES = ["i-01e3bf405aee2f613", "i-053b2f8c85c9a2573", "i-0685d6d40b619f7f5"]

class EC2_Service:
  def __init__(self, instances, show_logs = True):
    self.ec2 = boto3.client('ec2')
    self.instances = instances
    self.show_logs = show_logs

  def start_instances(self):
    try:
      result = self.ec2.start_instances(InstanceIds=self.instances)

      if self.show_logs:
        print("---")
        for instance in result['StartingInstances']:
          print(f"InstanceId: {instance['InstanceId']}")
          print(f"CurrentState: {instance['CurrentState']['Name']}")
          print(f"PreviousState: {instance['PreviousState']['Name']}")
          print("---")
    except Exception as error:
      print("Was not possible to start instances")
      print(f"[FAIL] {error}")

  def stop_instances(self):
    try:
      result = self.ec2.stop_instances(InstanceIds=self.instances)

      if self.show_logs:
        print("---")
        for instance in result['StoppingInstances']:
          print(f"InstanceId: {instance['InstanceId']}")
          print(f"CurrentState: {instance['CurrentState']['Name']}")
          print(f"PreviousState: {instance['PreviousState']['Name']}")
          print("---")
    except Exception as error:
      print("Was not possible to stop instances")
      print(f"[FAIL] {error}")

  def terminate_instances(self):
    try:
      result = self.ec2.terminate_instances(InstanceIds=self.instances)

      if self.show_logs:
        print("---")
        for instance in result['TerminatingInstances']:
          print(f"InstanceId: {instance['InstanceId']}")
          print(f"CurrentState: {instance['CurrentState']['Name']}")
          print(f"PreviousState: {instance['PreviousState']['Name']}")
          print("---")
    except Exception as error:
      print("Was not possible to terminate instances")
      print(f"[FAIL] {error}")

ec2_service = EC2_Service(INSTANCES)

# ec2_service.start_instances()
# ec2_service.stop_instances()
ec2_service.terminate_instances()
```

## Conclusion

In this class, we learned how to use the EC2 service using boto3. We saw how to start, stop and terminate an EC2 instance. We also saw how to use a class to encapsulate the operations.
