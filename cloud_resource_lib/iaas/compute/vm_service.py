import abc
class AbstractVMService(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def __init__(self,*args, **kwargs):
        pass
    
    @abc.abstractmethod
    def list_instances(self, *args, **kwargs):
        pass
    
    @abc.abstractmethod
    def list_instance_by_region(self, *args, **kwargs):
        pass
    
    #@abc.abstractmethod
    #def get_instance_by_id(self, *args,**kwargs):
    #    pass

    @abc.abstractmethod
    def create_instance(self, *args,**kwargs):
        pass

    @abc.abstractmethod
    def delete_instance_by_id(self, *args , **kwargs):
        pass

