# -*- coding: utf-8 -*-

import os
import MySQLdb as mdb

import utils


class ConfigNotFoundException(ImportError):
    msg = u"Chameleon was unable to find config file"


class ValidationError(Exception):
    pass


class Database(object):
    DEFAULTS = {
        'host': '127.0.0.1',
        'user': 'root',
        'port': 3306,
        'connect_timeout': 3,
        }

    conn = None

    def __init__(self, config=None):
        """
        if config is None => search filesystem tree up for 'chameleon_conf'
        module
        if config is string => load from file
        if config is kwargs => use it

        All keys from config go to MySQLdb.connect method.
        """
        if config is None:
            config = self.discover_config()

        if isinstance(config, str):
            config = utils.dict_from_module(config)

        if config is None:
            raise ConfigNotFoundException()

        self.config = config
        self.connect()

    def connect(self):
        cfg = self.DEFAULTS.copy()
        cfg.update(self.config['DATABASE'])
        self.conn = mdb.connect(**cfg)
        return self.conn

    def validate(self, name, value, *options):
        # TODO: stub
        if 'required' in options:
            if not value:
                raise ValidationError(u'Field "{}" is required'.format(name))

    # MySQLdb connection api

    def commit(self):
        return self.conn.commit()

    def rollback(self):
        return self.conn.rollback()

    def cursor(self, cls=None):
        return self.conn.cursor(cls)

    def discover_config(self):
        directory = os.path.dirname(os.path.abspath('.') + '/')
        name = 'chameleon_conf'
        config = None
        while config is None and directory:
            config = utils.dict_from_module(
                os.path.join(directory, name))
            directory = directory.rsplit(os.sep, 1)[0]

        return config
