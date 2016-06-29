# Flask-Zookeeper

The Flask-Zookeeper extension provides support to 
[Zookeeper](http://zookeeper.apache.org/) clusters.

## Quickstart

First, install Flask-Zookeeper using 
[pip](https://pip.pypa.io/en/stable/):

    $ pip install flask-zookeeper

Flask-Zookeeper depends, and will install for you, recent versions of 
Flask and [Kazzo](https://kazoo.readthedocs.io/en/latest/). 
Flask-Zookeeper is compatible with and tested on Python 2.7, 3.4 and 
3.5.

Next, add a `FlaskZookeeperClient` instance to your code:

```python
    from flask import Flask
    from flask_zookeeper import FlaskZookeeperClient
    
    app = Flask(__name__)
    
    fzc = FlaskZookeeperClient(app)
```

You can take a look at [tests/test_base](tests/test_base) for more 
complete example.

You can also take a look at 
[tests/test_blueprint](tests/test_blueprint) for an example using Flask's 
[application factories](http://flask.pocoo.org/docs/patterns/appfactories/) 
and [blueprints](http://flask.pocoo.org/docs/blueprints/).

## About setting up

Flask-Zookeeper uses additional variables which can be set in the 
`app.config`:

### Main values

* **KAZOO_HOSTS**: Zookeeper quorum server list separated by commas (
default: `127.0.0.1:2181`).
* **KAZOO_START_TIMEOUT**: Time in seconds to wait for connection to 
succeed (default: `15`).
* **KAZOO_SESSION_TIMEOUT**: The longest to wait for a Zookeeper 
connection (default: `10.0`).
* **KAZOO_RETRY**: Dict of options to use for retrying the connection 
to Zookeeper (default: `{'max_delay': 3600}`).

## ACL configuration

Zookeeper allow to set ACL. To enable this feature, set 
`KAZOO_ACL_USERNAME` and `KAZOO_ACL_PASSWORD` in the `app.config`.

* **KAZOO_ACL_USERNAME**: Username to use for the ACL.
* **KAZOO_ACL_PASSWORD**: A plain-text password to hash.
* **KAZOO_ACL_READ**: Read permission (default: `False`).
* **KAZOO_ACL_WRITE**: Write permission (default: `False`).
* **KAZOO_ACL_CREATE**: Create permission (default: `False`).
* **KAZOO_ACL_DELETE**: Delete permission (default: `False`).
* **KAZOO_ACL_ADMIN**: Admin permission (default: `False`).
* **KAZOO_ACL_ALL**: All permissions (default: `False`).

You can take a look at [tests/test_acl](tests/test_acl) for a 
complete example.

## License

Apache License 2.0