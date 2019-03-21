import requests

class client:
    
    def __init__(self):
        self.key = get_apikey()
        authenticate()
    
    def get_apikey(self):
        if not os.path.isfile('./config/access.conf'):
            logger.debug('Api Key not found. Getting user to enter it')
            apikey = input('Please enter your YNAB API key: ')
            apikeyEncoded = base64.b64encode(apikey)
            f = open('.config/access.conf', 'w')
            f.write()
            f.close()
            return apikey
        else:
            f = open('./config/access.conf', 'r')
            apikeyEncoded = f.read()
            f.close()
            return base64.b64decode(apikeyEncoded)

    def authenticate(self):
        url = 'api.youneedabudget.com'
