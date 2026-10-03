from http.client import responses
import requests
import json

from soupsieve.pretty import pretty

from yandex_token import ya_token

API_KEY = "at_MKOsUlxPf7IlnW7kXOP3oyId37LWk"
API_BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

def create_folder (key, url):
    ip = requests.get(f'{url}country?apiKey={key}').json()
    params = {'path': "Folder"}
    headers = {"Authorization": f"OAuth {ya_token}"}
    response = requests.put(f'{url}', params=params, headers=headers)
    return (response.status_code)

