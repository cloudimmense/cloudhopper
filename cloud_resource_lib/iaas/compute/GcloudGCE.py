import json
from vm_service import AbstractVMService
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

class GcloudGCE(AbstractVMService):

    def __init__(self, jsonfile):
        self.credential_type = "gce"
        creds_json = json.loads(open(jsonfile,"r").read())
        self.zone = "us-east1-b"
        ComputeEngine = get_driver(Provider.GCE)
        self.driver = ComputeEngine(creds_json["client_email"], jsonfile,
                       project=creds_json["project_id"])

    def get_driver_by_region(self, credentials, region_name):
        pass

    def list_instances(self, zone=None, *args, **kwargs):
        params = {}
        if zone:
            instances = self.driver.list_nodes(ex_zone=zone)
        else:
            instances = self.driver.list_nodes(ex_zone=zone)
        instances = [x.__dict__ for x in instances]
        return instances

    def list_instance_by_region(self, *args, **kwargs):
        pass

    def get_instance_by_id(self, *args, **kwargs):
        pass

    def create_instance(self, *args, **kwargs):
        pass

    def delete_instance_by_id(self, *args, **kwargs):
        pass

    def delete_instance_by_ids(self, *args, **kwargs):
        pass

    def stop_Instance(self, *args, **kwargs):
        pass

    def restart_Instance(self, *args, **kwargs):
        pass

    def get_size_object(self, driver, size_name):
        pass

    def get_image_object(self, driver, image_id):
        pass

    def get_sizes(self, driver):
        pass

    def get_nodes(self, driver):
        pass

    def get_locations(self):
        pass

    def get_Images(self, driver):
        pass

    def list_key_pairs(self, *args, **kwargs):
        pass
