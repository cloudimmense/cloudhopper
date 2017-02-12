import abc
class AbstractSaasStorageService(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self,*args, **kwargs):
        pass

    @abc.abstractmethod
    def list_folders(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def upload_folders(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def download_folders(self, *args,**kwargs):
        pass

    @abc.abstractmethod
    def delete_folders(self, *args,**kwargs):
        pass

    @abc.abstractmethod
    def list_files(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def upload_files(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def download_files(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete_files(self, *args, **kwargs):
        pass

