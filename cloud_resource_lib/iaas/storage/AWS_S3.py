from cloud_resource_lib.iaas.storage.iaas_storage_service import AbstractIaasStorageClass
from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver

class AWSS3(AbstractIaasStorageClass):
    def __init__(self, credentials, *args, **kwargs):
        self.credentials = credentials

    def get_driver_by_region(self, region_name):
        Driver = get_driver(Provider.S3)
        s3_driver = Driver(self.credentials["accessId"], self.credentials["secretKey"], region = region_name)
        self.s3_driver = s3_driver
        return s3_driver

    def list_containers(self, *args, **kwargs):
        driver = self.get_driver_by_region(kwargs["location"])
        containers = driver.list_containers()

        data = {}
        if containers:
            for i in containers:

                data = {}
                data['provider'] = i.name
                print(data['provider'])
                #data['service_provider'] = "AWS_EC2"
                #json_data = json.dumps(data)
                # all_nodes[loc] = self.list_instance_by_region(location=loc)
                #all_nodes[loc] = json_data
           # else:
                #data = {}
                #data['service_provider'] = "AWS_EC2"
                #data['nodes'] = "no nodes available"
                #all_nodes[loc] = data

        return containers

    def create_container(self, *args, **kwargs):
        driver = self.get_driver_by_region(kwargs["location"])
        container = driver.create_container(kwargs["name"])
        return container

    def get_container(self, *args, **kwargs):
        driver = self.get_driver_by_region(kwargs["location"])
        container = driver.get_container(kwargs["name"])
        return container

    def delete_container(self, *args, **kwargs):
        driver = self.get_driver_by_region(kwargs["location"])
        get_container_name = self.get_container(location = kwargs["location"], name = kwargs["name"])
        status = driver.delete_container(get_container_name)
        return status

    def upload_object(self, *args, **kwargs):
        driver = self.get_driver_by_region(kwargs["location"])
        namesplit = kwargs['upload_file_path'].split('/')
        object_name = namesplit[len(namesplit) - 1]
        container_object = self.get_container(location = kwargs["location"], name = kwargs["container_name"])
        status = driver.upload_object(kwargs['upload_file_path'], container_object, object_name)
        return status

    def list_container_objects(self, *args, **kwargs):
        driver = self.get_driver_by_region(kwargs["location"])
        container_object = self.get_container(location=kwargs["location"], name=kwargs["container_name"])
        #container_object = driver.get_container(kwargs["container_name"])
        list_objects = driver.list_container_objects(container_object)
        return list_objects

    def get_container_object(self, *args, **kwargs):
        driver = self.get_driver_by_region(kwargs["location"])
        get_container_object = driver.get_object(kwargs["container_name"], kwargs["object_name"])
        return get_container_object

    def download_object(self, *args, **kwargs):
        driver = self.get_driver_by_region(kwargs["location"])
        object_body = self.get_container_object(location = kwargs["location"], container_name = kwargs["container_name"], object_name = kwargs["object_name"])
        downloadedObject = driver.download_object(object_body, kwargs["download_file_location"], overwrite_existing = True, delete_on_failure = False)
        return downloadedObject

    def delete_object(self, *args, **kwargs):
        driver = self.get_driver_by_region(kwargs["location"])
        get_container_object = self.get_container_object(location = kwargs["location"], container_name = kwargs["container_name"], object_name = kwargs["object_name"])
        status = driver.delete_object(get_container_object)
        return status

    def list_containers_names(self, *args, **kwargs):
        driver = self.get_driver_by_region(kwargs["location"])
        containers = driver.list_containers()
        buckets = []
        for i in containers:
            buckets.append(i.name)
        return buckets

