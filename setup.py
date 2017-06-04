from setuptools import setup
from setuptools.command.install import install
from os.path import expanduser
from shutil import copyfile

setup(
    name='KeggImporter',
    version='0.1',
    author='Franca AF (Alexander da Franca Fernandes)',
    author_email='alexander@francafernandes.com.br',
    license='BSD',
    description='KEGG importer to relational database',
    long_description='KeggImporter get data from KeggReader and populate a PostgreSQL relational database.',
    packages=[ 'keggimporter' ],
    platforms='Linux',
    url='http://bioinfoteam.fiocruz.br/keggimporter',
    install_requires=[
            'configparser',
            'datetime ',
            'glob',
            'os',
            'pprint',
            're',
            'shutil',
            'sys',
            'unittest',
            ],
)


