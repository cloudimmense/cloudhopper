import abc
from base_auth import BaseAuth
class GcloudAuth(BaseAuth):    
    def __init__(self,name,path_to_json, **kwargs):
        self.name = name
        self.path_to_json = path_to_json
