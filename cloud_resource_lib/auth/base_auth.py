import abc
class BaseAuth(object):    
    @abc.abstractmethod
    def __init__(self,name,*args, **kwargs):
        pass
