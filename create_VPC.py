import boto3
from pprint import pprint

my_session = boto3.session.Session(profile_name='dolfined-dev')# Use a profile_name on your machine which has admin privileges
ec2_cli = my_session.client(service_name='ec2', region_name="us-east-1") #session for Clint
#ec2_resource = my_session.resource(service_name="ec2", region_name="us-east-1") #session for resource
new_vpc = ec2_cli.create_vpc(CidrBlock='10.0.0.0/16')
vpc_id = new_vpc['Vpc']['VpcId']
pprint(f"New VPC has been created successfully with id {vpc_id}")
#subnet = ec2.Subnet('id')