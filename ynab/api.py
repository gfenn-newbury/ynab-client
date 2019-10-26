import os
import logger
import base64
import requests


class auth:

    isAuthenticated = False

    def __init__(self, key='', logger=logger.getLogger()):
        self.logger = logger
        if key:
            self.key = key
        else:
            self.key = self.get_apikey()
        self.authenticate()

    def get_apikey(self):
        if not os.path.isfile('./config/access.conf') or not self.key:
            logger.debug('Api Key not found. Getting user to enter it')
            apikey = input('Please enter your YNAB API key: ')
            apikeyEncoded = base64.b64encode(apikey)
            f = open('.config/access.conf', 'w')
            f.write()
            f.close()
            return apikey
        elif not self.key:
            f = open('./config/access.conf', 'r')
            apikeyEncoded = f.read()
            f.close()
            return base64.b64decode(apikeyEncoded)
        else:
            return

    def authenticate(self):
        url = 'https://api.youneedabudget.com'
        h = {
            'Authorization': f'Bearer {self.key}',
            'Content-Type': 'application/json',
        }
        r = requests.get(url, headers=h)
        if r.status_code != '404':
            self.isAuthenticated = True

    def get_auth(self):
        return self.isAuthenticated
