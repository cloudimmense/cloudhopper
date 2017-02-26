import sys
sys.path.append("..")
import cloud_resource_lib as csrl
from aws_credentials import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from cloud_resource_lib import cloud_service_factory
from cloud_service_factory import CloudServiceFactory
auth = {
        'AWS_ACCESS_KEY_ID': AWS_ACCESS_KEY_ID,
        'AWS_SECRET_ACCESS_KEY': AWS_SECRET_ACCESS_KEY
        }
cloud_type = 'aws'
service = 'vm_service'
# creating a aws client from cloud service factory
csf = CloudServiceFactory()
aws_obj = csf.get_share_obj(cloud_type, service, auth)

