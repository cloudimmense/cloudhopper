from saas_storage_service import AbstractSaasStorageService
import dropbox

class Dropbox(AbstractSaasStorageService):
    def __init__(self, credentials, *args, **kwargs):
        self.credentials = credentials

    def get_client(self):
        client = dropbox.client.DropboxClient(self.credentials["access_token"])
        return client

    def list_folders(self, *args, **kwargs):
        pass

    def upload_folders(self, *args, **kwargs):
        pass

    def download_folders(self, *args, **kwargs):
        pass

    def delete_folders(self, *args, **kwargs):
        pass

    def list_files(self, *args, **kwargs):
        client = self.get_client()
        dir_metadata = client.metadata(kwargs["path"])
        listOfFiles = {}
        listOfFiles['dirs'] = []
        listOfFiles['files'] = []
        for content in dir_metadata['contents']:
            if content['is_dir']:
                listOfFiles['dirs'].append(content['path'])
            else:
                listOfFiles['files'].append(content['path'])
        return listOfFiles

    def upload_files(self, *args, **kwargs):
        client = self.get_client()
        f = open(kwargs['file'], 'rb')
        namesplit = kwargs['file'].split('/')
        uploadFPath = kwargs['path'] + namesplit[len(namesplit) - 1]
        response = client.put_file(uploadFPath, f)
        return response

    def download_files(self, *args, **kwargs):
        client = self.get_client()
        namesplit = kwargs['dropbox_file'].split('/')
        filename = namesplit[len(namesplit) - 1]
        dfile = open(kwargs['download_file_location']+'/'+filename, 'wb')
        with client.get_file(kwargs['dropbox_file']) as f:
            dfile.write(f.read())
        dfile.close()
        return 'Downloaded'

    def delete_files(self, *args, **kwargs):
        client = self.get_client()
        response = client.file_delete(kwargs["dropbox_file"])
        return response

