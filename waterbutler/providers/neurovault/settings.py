try:
    from waterbutler import settings
except ImportError:
    settings = {}

config = settings.get('NEUROVAULT_PROVIDER_CONFIG', {})

BASE_URL = config.get('BASE_URL', 'http://neurovault.org/api/')
VIEW_URL = config.get('VIEW_URL', 'http://neurovaul.torg/')
