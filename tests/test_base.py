#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
import unittest
from flask import Flask
from flask_zookeeper import FlaskZookeeperClient


class BaseConfig:
    KAZOO_HOSTS = "10.46.3.92:2181"


class ZookeeperTestCase(unittest.TestCase):
    def test_simple_connect(self):
        app = Flask(__name__)
        app.config.from_object(BaseConfig)
        fzc = FlaskZookeeperClient()
        fzc.init_app(app)

        with app.app_context():
            self.assertIsNotNone(fzc.connection)
            self.assertIsInstance(fzc.connection.get_children('/'), list)


if __name__ == '__main__':
    unittest.main()
