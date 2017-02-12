from cloud_resource_lib.iaas.storage.iaas_storage_service import AbstractIaasStorageClass
from libcloud.storage.drivers.google_storage import GoogleStorageDriver
import os

class google_storage(AbstractIaasStorageClass):
    def __init__(self, credentials, *args, **kwargs):
        self.credentials = credentials
        self.credentials_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        self.credentials_path += "/credentials/" + credentials['json_file']

    def get_driver(self):
        driver = GoogleStorageDriver(self.credentials['client_email'], self.credentials_path, project=self.credentials["project_id"])
        return driver

    def list_containers(self, *args, **kwargs):
        driver = self.get_driver()
        containers = driver.list_containers()
        return containers

    def create_container(self, *args, **kwargs):
        driver = self.get_driver()
        container = driver.create_container(kwargs["name"])
        return container

    def get_container(self, *args, **kwargs):
        driver = self.get_driver()
        container = driver.get_container(kwargs["name"])
        return container

    def delete_container(self, *args, **kwargs):
        driver = self.get_driver()
        get_container_name = self.get_container(name=kwargs["name"])
        status = driver.delete_container(get_container_name)
        return status

    def upload_object(self, *args, **kwargs):
        driver = self.get_driver()
        namesplit = kwargs['upload_file_path'].split('/')
        object_name = namesplit[len(namesplit) - 1]
        container_object = self.get_container(name=kwargs["container_name"])
        status = driver.upload_object(kwargs['upload_file_path'], container_object, object_name)
        return status

    def list_container_objects(self, *args, **kwargs):
        driver = self.get_driver()
        container_object = self.get_container(name=kwargs["container_name"])
        list_objects = driver.list_container_objects(container_object)
        return list_objects

    def get_container_object(self, *args, **kwargs):
        driver = self.get_driver()
        get_container_object = driver.get_object(kwargs["container_name"], kwargs["object_name"])
        return get_container_object

    def download_object(self, *args, **kwargs):
        driver = self.get_driver()
        object_body = self.get_container_object(container_name=kwargs["container_name"],
                                                object_name=kwargs["object_name"])
        downloadedObject = driver.download_object(object_body, kwargs["download_file_location"],
                                                  overwrite_existing=True, delete_on_failure=False)
        return downloadedObject

    def delete_object(self, *args, **kwargs):
        driver = self.get_driver()
        get_container_object = self.get_container_object(container_name=kwargs["container_name"], object_name=kwargs["object_name"])
        status = driver.delete_object(get_container_object)
        return status

    def list_containers_names(self, *args, **kwargs):
        driver = self.get_driver()
        containers = driver.list_containers()
        buckets = []
        for i in containers:
            buckets.append(i.name)
        return buckets
