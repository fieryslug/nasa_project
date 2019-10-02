import params
import secret
import requests

def make_request(api_name, extra):
    extra['api_key'] = secret.key
    r = requests.get('https://api.nasa.gov/{}'.format(api_name), extra)
    return r.content

