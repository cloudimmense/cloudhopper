from vm_service import AbstractVMService
import json

class AWSEC2(AbstractVMService):

    def __init__(self):
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

    def get_driver_by_region(self, credentials, region_name):
        instance = {"instance_id": "abc123"}
        return instances

    def list_instances(self, *args, **kwargs):
        instances = [ {"instance_id": "abc123"}, {"instance_id": "ajnbd23434"}]
        return instances

    def list_instance_by_region(self, *args, **kwargs):
        instances = [ {"instance_id": "abc123"}, {"instance_id": "ajnbd23434"}]
        return instances

    def get_instance_by_id(self, *args, **kwargs):
        instance = {"instance_id": "abc123"}
        return instance

    def create_instance(self, *args, **kwargs):
        instance = {"instance_id": "abc123"}
        return instance

    def delete_instance_by_id(self, *args, **kwargs):
        instance = {"instance_id": "abc123"}
        return instance

    def stop_Instance(self, *args, **kwargs):
        instance = {"instance_id": "abc123"}
        return instance

    def restart_Instance(self, *args, **kwargs):
        instance = {"instance_id": "abc123"}
        return instance

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
