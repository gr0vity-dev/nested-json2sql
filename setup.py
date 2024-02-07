from setuptools import setup, find_packages
from nestedjson2sql import __version__

setup(
    name='nestedjson2sql',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'json-relational>=0.0.3',
        'sqlalchemy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'json2sql=nestedjson2sql.main:main',
        ],
    },
)
