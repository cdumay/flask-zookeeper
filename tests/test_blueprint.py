#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""

from flask import Flask
from flask import Blueprint
from flask_zookeeper import FlaskZookeeperClient

class BaseConfig:
    KAZOO_HOSTS = "10.46.3.92:2181"

# flask app init
app = Flask(__name__)
app.config.from_object(BaseConfig)

# Zookeeper blueprint
zkc = Blueprint('zookeeper-client', __name__)
zk_client = FlaskZookeeperClient(zkc)

# blueprint register
app.register_blueprint(zkc)

with app.app_context():
    print(zk_client.connection.get_children('/'))
