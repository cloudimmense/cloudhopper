import abc
class AbstractIaasStorageClass(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self,*args, **kwargs):
        pass

    @abc.abstractmethod
    def list_containers(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def create_container(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_container(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete_container(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def upload_object(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def list_container_objects(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_container_object(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def download_object(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete_object(self, *args, **kwargs):
        pass
