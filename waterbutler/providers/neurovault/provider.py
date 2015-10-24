from waterbutler.core import provider
from waterbutler.providers.NeuroVault import settings


class NeuroVaultProvider(provider.BaseProvider):

    NAME = 'NeuroVault'
    BASE_URL = settings.BASE_URL

    def __init__(self, auth, credentials, settings):
        # Placeholder
        super().__init__(auth, credentials, settings)
        self.token = self.credentials['token']
        self.collection = self.settings['collection']

    def upload(self, stream, **kwargs):
        pass

    def delete(self, **kwargs):
        pass

    def metadata(self, **kwargs):
        pass

    def validate_path(self, path, **kwargs):
        pass
