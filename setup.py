from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='YNAB Client',
    version='0.5.2',
    description='Python YNAB API Client',
    long_description=readme,
    author='Guy Newbury',
    author_email='guyn@live.co.uk',
    url='https://github.com/gnewbury1/ynab-client',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
