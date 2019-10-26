import logging
import logging.handlers
from ynab import api


def setupLogging():
    logger = logging.getLogger('YNABPython')
    logger.setLevel(logging.DEBUG)

    fh = logging.handlers.SysLogHandler(address='./ynab.log')

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    fh.setFormatter(formatter)
    logger.addHandler(fh)


def main():
    logger = setupLogging()
    api.auth(key='', logger=logger)


if __name__ == '__main__':
    main()
