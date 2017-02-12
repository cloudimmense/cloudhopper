from vm_service import AbstractVMService
import json

class GcloudGCE(AbstractVMService):
    def __init__(self):
        #self.credentials = credentials
        #self.credentials = args[0]
        #print self.credentials
        self.credential_type = "gce"
        self.locations = [
            "us-east-1",
            "us-west-2",
            "us-west-1",
            "eu-west-1",
            "eu-central-1",
            "ap-southeast-1",
            "ap-northeast-1",
            "ap-southeast-2",
            #"ap-northeast-2",
            "sa-east-1"]

    def get_driver_by_region(self, credentials, region_name):
        pass
    def list_instances(self, *args, **kwargs):
        instances = [ {"instance_id": "abc123"}, {"instance_id": "ajnbd23434"}]
        return instances
    def list_instance_by_region(self, *args, **kwargs):
        pass
    def get_instance_by_id(self, *args, **kwargs):
        pass
    def create_instance(self, *args, **kwargs):
        pass
    def delete_instance_by_id(self, *args, **kwargs):
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
