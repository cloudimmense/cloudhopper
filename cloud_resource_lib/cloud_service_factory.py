import auth
from cloud_resource_lib.iaas.compute import AWSEC2
from cloud_resource_lib.iaas.compute import OpenstackServer
from cloud_resource_lib.iaas.compute import GcloudGCE

class CloudServiceFactory(object):
    service_classes = {
        "aws":{ "vm_service": AWSEC2.AWSEC2 },
        "openstack":{ "vm_service": OpenstackServer.OpenstackServer },
        "gcloud":{ "vm_service": GcloudGCE.GcloudGCE },

    }
    @staticmethod
    def get_share_obj(cloud_type, service, auth):
        share_class = CloudServiceFactory.service_classes[cloud_type][service]
        if share_class:
            return share_class(auth)
        raise NotImplementedError("The requested sharing has not been implemented")
    
    def __init__(self):
        pass
