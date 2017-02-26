import json
import boto3
import time
from vm_service import AbstractVMService

class AWSEC2(AbstractVMService):

    def __init__(self, auth):
        self.credential_type =  "aws"
        self.locations = [
            "us-east-1",
            "us-west-2",
            "us-west-1",
            "eu-west-1",
            "eu-central-1",
            "ap-southeast-1",
            "ap-northeast-1",
            "ap-southeast-2",
            "sa-east-1"]
        self.auth = auth
        self.client = boto3.resource(
                 'ec2',
                 # Hard coded strings as credentials, not recommended.
                 aws_access_key_id = auth['AWS_ACCESS_KEY_ID'],
                 aws_secret_access_key = auth['AWS_SECRET_ACCESS_KEY'],
                 region_name = self.locations[0]
        )

    def get_client(self, region='us-east-1'):
        client = boto3.resource(
                 'ec2',
                 aws_access_key_id = self.auth['AWS_ACCESS_KEY_ID'],
                 aws_secret_access_key = self.auth['AWS_SECRET_ACCESS_KEY'],
                 region_name = region
        )
        return client

    def list_instances(self, *args, **kwargs):
        params = {}
        if kwargs.get('filters', None):
            params["Filters"] = filters
        if kwargs.get('dryrun', None):
            params["DryRun"] = dryrun
        if kwargs.get('region', None):
            client = self.get_client(kwargs.get('region', None))
        else:
            client = self.client
        instances = []
        instances_call = client.instances.filter()
        """
        all the parameters listed below are subjected to change
        based on requirements.
        Currently lists instance dicts with public_ip and domain name
        """
        for instance in instances_call:
            inst = {}
            inst['id'] = instance.id
            inst['public_dns_name'] = instance.public_dns_name 
            inst['public_ip_address'] = instance.public_ip_address
            instances.append(inst)
        return instances

    def list_regions(self, *args, **kwargs):
        client = self.client
        regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
        return regions
        
    def list_instance_by_region(self, *args, **kwargs):
        instances = [ {"instance_id": "abc123"}, {"instance_id": "ajnbd23434"}]
        return instances

    def get_instance_by_id(self, *args, **kwargs):
        instance = {"instance_id": "abc123"}
        return instance

    def create_instance(self, *args, **kwargs):
        # samplecode
        """
        instance = ec2.create_instances(
                   DryRun=True|False,
                   ImageId='string',
                   MinCount=123,
                   MaxCount=123,
                   KeyName='string',
                   SecurityGroups=[
                       'string',
                   ],
                   SecurityGroupIds=[
                       'string',
                   ],
                   UserData='string',
                   InstanceType='t2.micro',
                   Placement={
                   'AvailabilityZone': 'string',
                   'GroupName': 'string',
                   'Tenancy': 'default'|'dedicated'|'host',
                   'HostId': 'string',
                   'Affinity': 'string'
                   },
                   KernelId='string',
                   RamdiskId='string',
                   BlockDeviceMappings=[
                   {
                       'VirtualName': 'string',
                       'DeviceName': 'string',
                       'Ebs': {
                               'SnapshotId': 'string',
                               'VolumeSize': 123,
                               'DeleteOnTermination': True|False,
                               'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
                               'Iops': 123,
                               'Encrypted': True|False
                              },
                       'NoDevice': 'string'
                   },
              ],
              Monitoring={
                  'Enabled': True|False
              },
              SubnetId='string',
              DisableApiTermination=True|False,
              InstanceInitiatedShutdownBehavior='stop'|'terminate',
              PrivateIpAddress='string',
              Ipv6Addresses=[
                  {
                  'Ipv6Address': 'string'
                  },
              ],
              Ipv6AddressCount=123,
              ClientToken='string',
              AdditionalInfo='string',
              NetworkInterfaces=[
              {
                'NetworkInterfaceId': 'string',
                'DeviceIndex': 123,
                'SubnetId': 'string',
                'Description': 'string',
                'PrivateIpAddress': 'string',
                'Groups': [
                    'string',
                ],
                'DeleteOnTermination': True|False,
                'PrivateIpAddresses': [
                    {
                        'PrivateIpAddress': 'string',
                        'Primary': True|False
                    },
                ],
                'SecondaryPrivateIpAddressCount': 123,
                'AssociatePublicIpAddress': True|False,
                'Ipv6Addresses': [
                    {
                        'Ipv6Address': 'string'
                    },
                ],
                'Ipv6AddressCount': 123
            },
        ],
        IamInstanceProfile={
            'Arn': 'string',
            'Name': 'string'
        },
        EbsOptimized=True|False
        )
        """
        params = {}
        params['ImageId'] = image_id
        if dry_run:
            params['DryRun'] = dry_run
        if min_count:
            params['MinCount'] = min_count
        if max_count:
            params['MaxCount'] = max_count
        else:
            params['MaxCount'] = 1
        if key_name:
            params['KeyName'] = key_name
        if isinstance(security_groups, str):
            params['SecurityGroups'] = [ security_groups]
        elif  isinstance(security_groups, list):
            params['SecurityGroups'] = security_groups
        if isinstance(security_group_ids, str):
            params['SecurityGroupsIds'] = [ security_group_ids ]
        elif isinstance(security_groups_ids, list):
            params['SecurityGroupsIds'] = security_group_ids
        if user_data:
            params['UserData'] = user_data
        if placement:
            params['Placement'] = placement
        if kernel_id:
            params['KernelId'] = kernel_id
        if ramdisk_id:
            params['RamdiskId'] = ramdisk_id
        if blockdevice_mappings:
            params['BlockDeviceMappings'] = blockdevice_mappings
        if monitoring:
            params[' Monitoring'] = { 'Enabled': monitoring }
        if subnet_id:
            params['SubnetId'] = subnet_id
        if disable_api_termination:
            params['DisableApiTermination'] = disable_api_termination
        if instance_initiated_shutdown_behaviour:
            params['InstanceInitiatedShutdownBehavior'] = instance_initiated_shutdown_behaviour
        if private_ip_address:
            params['PrivateIpAddress'] = private_ip_address
        if isinstance(ipv6_addresses, list):
            params['Ipv6Addresses'] = ipv6_addresses
        elif isinstance(ipv6_addresses, str):
            params['Ipv6Addresses'] = [ {'Ipv6Address': ipv6_addresses} ]
        if Ipv6Address:
            params['Ipv6AddressCount'] = ipv6_address_count,
        if client_token:
            params['ClientToken'] = client_token
        if additional_info:
            params['AdditionalInfo'] = additional_info
        if network_interfaces:
            params['NetworkInterfaces'] = network_interfaces
        if iam_instace_profile:
            params['iam_instance_profile'] = iam_instace_profile
        if ebs_optimized:
            params['EbsOptimized'] = ebs_optimized
        
        instances = self.client.create_instances(**params)
        return instances

    def delete_instance_by_ids(self, *args, **kwargs):
        """
        response = client.terminate_instances(
           DryRun=True|False,
           InstanceIds=[
              'string',
           ]
         )
        """
        
        if wait:
            self.client.terminate_instances(InstanceIds=ids)
            self.wait_for_state(ids, "terminated")        
        else:
            self.client.instances.filter(InstanceIds=ids).terminate()
    
    def wait_for_state(self, ids, state):
        count = 10
        res = self.client.describe_instance_status(InstanceIds=ids)
        states = [x["InstanceState"]['Name'] for x in res["InstanceStatuses"]]
        while count >=0:
            if len(set(states)) > 1:
                time.sleep(10)
                count = count - 1
        if count == 0:
            return False 
        return True

    def stop_Instances(self, *args, **kwargs):
        """
        response = client.stop_instances(
                   DryRun=True|False,
                   InstanceIds=[
                   'string',
                   ],
                   Force=True|False
                  )
        """
        instance = {"instance_id": "abc123"}
        if wait:
            self.client.stop_instances(InstanceIds=ids)
            self.wait_for_state(ids, "stopped")        
        else:
            self.client.stop_instances(InstanceIds=ids)
        return instance
    
    def start_Instances(self, *args, **kwargs):
        """
        response = client.start_instances(
                   DryRun=True|False,
                   InstanceIds=[
                   'string',
                   ],
                   Force=True|False
                  )
        """
        instance = {"instance_id": "abc123"}
        if wait:
            self.client.start_instances(InstanceIds=ids)
            self.wait_for_state(ids, "running")        
        else:
            self.client.start_instances(InstanceIds=ids)
        return instance

    def restart_Instances(self, *args, **kwargs):
        self.stop_instances(ids=ids)
        self.start_instances(ids=ids)
        
    def get_size_object(self, driver, size_name):
        instance = {"instance_id": "abc123"}
        return instance

    def get_image_object(self, driver, image_id):
        instance = {"instance_id": "abc123"}
        return instance

    def get_sizes(self, driver):
        instance = [{"instance_id": "abc123"}]
        return instance

    def get_nodes(self, driver):
        instance = [{"instance_id": "abc123"}]
        return instance

    def get_locations(self):
        instance = [{"instance_id": "abc123"}]
        return instance

    def get_Images(self, driver):
        instance = [{"instance_id": "abc123"}]
        return instance

    def list_key_pairs(self, *args, **kwargs):
        instance = [{"instance_id": "abc123"}]
        return instance
