# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>

"""

from setuptools import setup, find_packages

setup(
    name='flask-zookeeper',
    version=open('VERSION', 'r').read().strip(),
    description="Flask Zookeeper client",
    long_description=open('README.rst', 'r').read().strip(),
    classifiers=["Programming Language :: Python"],
    keywords='',
    author='Cedric DUMAY',
    author_email='cedric.dumay@gmail.com',
    url='https://github.com/cdumay/flask-zookeeper',
    license='Apache License',
    py_modules=['flask_zookeeper'],
    include_package_data=True,
    zip_safe=True,
    install_requires=open('requirements.txt', 'r').readlines(),
    package_dir={'': 'src'},
    packages=find_packages('src'),
)
