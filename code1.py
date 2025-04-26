import boto3

def launch_ec2_with_cloudformation(template_body, stack_name):
  client = boto3.client('cloudformation')
  response = client.create_stack(
    StackName=stack_name,
    TemplateBody=template_body,
    Capabilities=['CAPABILITY_NAMED_IAM']
  )
  print(f"Stack creation initiated: {response['StackId']}")

# Example usage
template_body = """
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
  "MyEC2Instance": {
    "Type": "AWS::EC2::Instance",
    "Properties": {
    "InstanceType": "t2.micro",
    "ImageId": "ami-0abcdef1234567890"
    }
  }
  }
}
"""
launch_ec2_with_cloudformation(template_body, "MyEC2Stack")