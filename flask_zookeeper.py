#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
import uuid

from flask import current_app
from flask.signals import Namespace
from flask.blueprints import Blueprint
from kazoo.client import KazooClient
from kazoo.security import make_digest_acl

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

__all__ = (
    'FlaskZookeeperClient',
)

connection_state_changed = Namespace().signal('state-change')


class FlaskZookeeperClient(object):
    def __init__(self, app=None):
        self.uuid = uuid.uuid4()
        self.app = None
        self.blueprint = None
        self.blueprint_setup = None

        if app is not None:
            self.app = app
            self.init_app(app)

    def init_app(self, app):
        if isinstance(app, Blueprint):
            app.record(self._deferred_blueprint_init)
        else:
            self._init_app(app)

    def _deferred_blueprint_init(self, setup_state):
        self._init_app(setup_state.app)

    def _init_app(self, app):
        """Initialize the `app` for use with this
        :class:`~FlaskZookeeperClient`. This is called automatically if `app`
        is passed to :meth:`~FlaskZookeeperClient.__init__`.

        :param app: Flask application instance.
        """
        app.config.setdefault('KAZOO_HOSTS', '127.0.0.1:2181')
        app.config.setdefault('KAZOO_START_TIMEOUT', 15)
        app.config.setdefault('KAZOO_SESSION_TIMEOUT', 10.0)
        app.config.setdefault('KAZOO_RETRY', {'max_delay': 3600})  # 1 hour

        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def connect(self):
        """Initialize a connection to the Zookeeper quorum.

        :return: Kazoo client object as connection.
        """
        client_kwargs = dict(
            hosts=current_app.config['KAZOO_HOSTS'],
            timeout=current_app.config['KAZOO_SESSION_TIMEOUT'],
            connection_retry=current_app.config['KAZOO_RETRY'],
            command_retry=current_app.config['KAZOO_RETRY']
        )
        # is ACL ?
        username = current_app.config.get('KAZOO_ACL_USERNAME', None)
        password = current_app.config.get('KAZOO_ACL_PASSWORD', None)

        if username and password:
            client_kwargs.update(dict(
                default_acl=[
                    make_digest_acl(
                        username=username,
                        password=password,
                        read=current_app.config.get(
                            'KAZOO_ACL_READ', False
                        ),
                        write=current_app.config.get(
                            'KAZOO_ACL_WRITE', False
                        ),
                        create=current_app.config.get(
                            'KAZOO_ACL_CREATE', False
                        ),
                        delete=current_app.config.get(
                            'KAZOO_ACL_DELETE', False
                        ),
                        admin=current_app.config.get(
                            'KAZOO_ACL_ADMIN', False
                        ),
                        all=current_app.config.get(
                            'KAZOO_ACL_ALL', False
                        )

                    )
                ],
                auth_data=[("digest", ":".join((username, password)))],
            ))

        client = KazooClient(**client_kwargs)
        client.start(timeout=current_app.config['KAZOO_START_TIMEOUT'])
        client.add_listener(self.connection_state_listener)
        return client

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'kazoo_client'):
            ctx.kazoo_client.stop()
            ctx.kazoo_client.close()

    @property
    def connection(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, self.uuid):
                setattr(ctx, self.uuid, self.connect())
            return getattr(ctx, self.uuid)

    def connection_state_listener(self, state):
        """Publishes state changes to a Flask signal"""
        connection_state_changed.send(self, state=state)
