.. image:: https://travis-ci.org/cdumay/flask-zookeeper.svg?branch=master
    :target: https://travis-ci.org/cdumay/flask-zookeeper

Flask-Zookeeper
===============

The Flask-Zookeeper extension provides support to 
`Zookeeper <http://zookeeper.apache.org/>`_ clusters.

Quickstart
----------

First, install cdumay-rest-client using
`pip <https://pip.pypa.io/en/stable/>`_:

    pip install flask-zookeeper

Flask-Zookeeper depends, and will install for you, recent versions of 
Flask and `Kazzo <https://kazoo.readthedocs.io/en/latest/>`_.
Flask-Zookeeper is compatible with and tested on Python 2.7, 3.4 and 3.5.

Next, add a :code:`FlaskZookeeperClient` instance to your code:

.. code-block:: python

    from flask import Flask
    from flask_zookeeper import FlaskZookeeperClient
    
    app = Flask(__name__)
    fzc = FlaskZookeeperClient(app)

You can take a look at `tests/test_base.py <tests/test_base.py>`_ for more
complete example. 

You can also take a look at 
`tests/test_blueprint.py <tests/test_blueprint.py>`_ for an example using Flask's
`application factories <http://flask.pocoo.org/docs/patterns/appfactories/>`_
and `blueprints <http://flask.pocoo.org/docs/blueprints/>`_.

About setting up
----------------

Flask-Zookeeper uses additional variables which can be set in the 
`app.config`:

Main values
***********

* **KAZOO_HOSTS**: Zookeeper quorum server list separated by commas (default: :code:`127.0.0.1:2181`).
* **KAZOO_START_TIMEOUT**: Time in seconds to wait for connection to succeed (default: :code:`15`).
* **KAZOO_SESSION_TIMEOUT**: The longest to wait for a Zookeeper connection (default: :code:`10.0`).
* **KAZOO_RETRY**: Dict of options to use for retrying the connection to Zookeeper (default: :code:`{'max_delay': 3600}`).

ACL configuration
*****************

Zookeeper allow to set ACL. To enable this feature, set 
:code:`KAZOO_ACL_USERNAME` and :code:`KAZOO_ACL_PASSWORD` in the :code:`app.config`.

* **KAZOO_ACL_USERNAME**: Username to use for the ACL.
* **KAZOO_ACL_PASSWORD**: A plain-text password to hash.
* **KAZOO_ACL_READ**: Read permission (default: :code:`False`).
* **KAZOO_ACL_WRITE**: Write permission (default: :code:`False`).
* **KAZOO_ACL_CREATE**: Create permission (default: :code:`False`).
* **KAZOO_ACL_DELETE**: Delete permission (default: :code:`False`).
* **KAZOO_ACL_ADMIN**: Admin permission (default: :code:`False`).
* **KAZOO_ACL_ALL**: All permissions (default: :code:`False`).

You can take a look at `tests/test_acl.py <tests/test_acl.py>`_ for a
complete example.

License
-------

Apache License 2.0
