import sys
import os
sys.path.append("..")
import cloud_resource_lib as csrl
from cloud_resource_lib import cloud_service_factory
from cloud_service_factory import CloudServiceFactory
cloud_type = 'gcloud'
service = 'vm_service'
# add you json file path
jsonfile = 'allperms.json'
jsonfile = os.path.abspath(jsonfile)
# creating a aws client from cloud service factory
csf = CloudServiceFactory()
gcloud_obj = csf.get_share_obj(cloud_type, service, jsonfile)
# usage with out zone
print(gcloud_obj.list_instances())
# usage with zone
print(gcloud_obj.list_instances(zone="us-east1-b"))
