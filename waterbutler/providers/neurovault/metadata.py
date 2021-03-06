from waterbutler.core import metadata


class BaseNeuroVaultMetadata:

    @property
    def provider(self):
        return 'neurovault'


class NeuroVaultImageMetadata(BaseNeuroVaultMetadata, metadata.BaseFileMetadata):

    def __init__(self, raw):
        super().__init__(raw)

    @property
    def kind(self):
        return 'file'

    @property
    def path(self):
        return self.build_path(self.raw['id'])

    @property
    def materialized_path(self):
        return self.build_path(self.raw['title'])

    @property
    def name(self):
        return self.raw['title']

    @property
    def size(self):
        return self.raw['bytes']

    @property
    def modified(self):
        return self.raw['modify_date']

    @property
    def content_type(self):
        return self.raw['content_type']

    @property
    def id(self):
        return self.raw['id']

    @property
    def file(self):
        return self.raw['file']

    @property
    def collection_id(self):
        return self.raw['collection_id']

    @property
    def map_type(self):
        return self.raw['map_type']

    @property
    def description(self):
        return self.raw['description']

    @property
    def image_type(self):
        return self.raw['image_type']

    @property
    def web_view(self):
        return self.raw['url']


class NeuroVaultCollectionMetadata(BaseNeuroVaultMetadata, metadata.BaseMetadata):

    def __init__(self, raw):
        super().__init__(raw)

    @property
    def kind(self):
        return 'folder'

    @property
    def path(self):
        return self.build_path(self.raw['id'])

    @property
    def materialized_path(self):
        return self.build_path(self.raw['title'])

    @property
    def modified(self):
        return self.raw['modify_date']

    @property
    def id(self):
        return self.raw['id']

    @property
    def name(self):
        return self.raw['name']

    @property
    def description(self):
        return self.raw['description']

    @property
    def owner_name(self):
        return self.raw['owner_name']

    @property
    def doi(self):
        return self.raw['DOI']

    @property
    def authors(self):
        return self.raw['authors']

    @property
    def web_view(self):
        return self.raw['url']
