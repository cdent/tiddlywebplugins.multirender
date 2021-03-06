
import os
from setuptools import setup, find_packages

VERSION = '0.1'

setup(
        namespace_packages = ['tiddlywebplugins'],
        name = 'tiddlywebplugins.multirender',
        version = VERSION,
        description = 'A TiddlyWeb plugin to dispatch one of several wikitext rendering systems.',
        long_description=file(os.path.join(os.path.dirname(__file__), 'README')).read(),
        author = 'Chris Dent',
        url = 'http://pypi.python.org/pypi/tiddlywebplugins.multirender',
        packages = find_packages(exclude=['test']),
        author_email = 'cdent@peermore.com',
        platforms = 'Posix; MacOS X; Windows',
        install_requires = ['setuptools', 'tiddlyweb'],
        zip_safe = False,
        )
