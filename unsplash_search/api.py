from unsplash.api import Api
from unsplash.auth import Auth
import os.path
import json
from django.core.exceptions import ImproperlyConfigured

def get_secret(setting):
    """Возвращает значение setting из файла unsplash_api.json"""
    if os.path.exists('unsplash_api.json'):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        key = os.path.join(BASE_DIR, "unsplash_api.json")
        with open(key) as f:
            secrets = json.loads(f.read())
        try:
            return secrets[setting]
        except KeyError:
            error_msg = "Set the {} environment variable".format(setting)
            raise ImproperlyConfigured(error_msg)
    else:
        return os.environ[setting]


client_id = get_secret("client_id")
client_secret = get_secret("client_secret")
redirect_uri = get_secret("redirect_uri")
code = ""

unsplash_auth = Auth(client_id, client_secret, redirect_uri, code=code)
unsplash_api = Api(unsplash_auth)