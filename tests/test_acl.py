#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
import unittest
from kazoo import exceptions
from flask import Flask
from flask_zookeeper import FlaskZookeeperClient


class Config:
    KAZOO_HOSTS = "10.46.3.92:2181"
    KAZOO_ACL_USERNAME = "admin"
    KAZOO_ACL_PASSWORD = "admin"


class ZookeeperACLTestCase(unittest.TestCase):
    app = None

    @classmethod
    def setUpClass(cls):
        ZookeeperACLTestCase.app = Flask(__name__)
        ZookeeperACLTestCase.app.config.from_object(Config)

    def test_read_error(self):
        fzc = FlaskZookeeperClient(self.app)
        with self.app.app_context():
            self.assertRaises(
                exceptions.NoAuthError,
                fzc.connection.get,
                '/'
            )


if __name__ == '__main__':
    unittest.main()
