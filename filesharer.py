from filestack import Client

class FileSharer:

    def __init__(self, filepath, api_key='Aypax5pyQ1CWK2Y4jLK3Yz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_fileLink = client.upload(filepath= self.filepath)
        return new_fileLink.url