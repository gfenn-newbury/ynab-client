import os
import base64
import logging
import logging.handlers
from ynab.objects import transaction
from ynab.api import client

logger = logging.getLogger('YNABPython')
logger.setLevel(logging.DEBUG)

fh = logging.handlers.SysLogHandler(address = '/dev/log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

def connect_api():
    ynab()

def main():
    #api = connect_api()
    trans = transaction('01/01/19','test','category:test','0.00','1.00','test')
    print(trans.to_dict())

if __name__ == '__main__':
    main()
