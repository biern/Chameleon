# -*- coding: utf-8 -*-

import inspect

from chameleon import utils
from chameleon.db import Database


class DBCommandWrapper(object):
    def __init__(self):
        args, varargs, keywords, defaults = inspect.getargspec(
            self.perform.im_func)

        self.defaults = defaults or []
        self.args = args[:-len(defaults)] if defaults else args
        self.keyword_args = args[-len(defaults):]

    def __call__(self, db, *args, **kwargs):
        """
        Calls :attr:`perform` as an unbound function.
        """
        with db.conn:
            self.perform.im_func(db, *args, **self.add_defaults(db, kwargs))

    def add_defaults(self, db, kwargs):
        """
        Adds values from 'DEFAULT_ARGS' config to keyword args if they where
        not supplied explicitly
        """
        res = kwargs.copy()
        for k, v in self.get_config_default_args(db).items():
            res.setdefault(k, v)

        return res

    def get_parser(self, db=None):
        parser = utils.parser_from_func(
            self.perform, skip=1,
            override_defaults=self.get_config_default_args(db))

        return parser

    def get_config_default_args(self, db):
        """
        Returns dict of args found in db.config['DEFAULT_ARGS'] that match
        keywords of this command.
        """
        return dict(
            (k, v) for k, v in db.config.get('DEFAULT_ARGS', {}).items() if \
                k in self.keyword_args)

    def shell_eval(self, argv=None):
        db = Database()
        parser = self.get_parser(db=db)
        args = parser.parse_args(argv)
        return self.call_from_namespace(db, args)

    def args_from_namespace(self, namespace):
        """
        Returns ordered argument list for :meth:`perform`
        based on namespace returned by ``self.get_parser().parse_args()``.
        """
        args, varargs, keywords, defaults = inspect.getargspec(
            self.perform.im_func)
        return [getattr(namespace, name) for name in args if name != 'db'] + \
            (getattr(namespace, varargs, []) if varargs else [])

    def call_from_namespace(self, db, namespace):
        """
        Transletes namespace to :meth:`perform` arguments and calls it.
        """
        self(db, *self.args_from_namespace(namespace))

    @classmethod
    def for_func(cls, func):
        """
        Creates wrapper instance suited for `func`
        """
        return cls.create_descendant(func)()

    @classmethod
    def create_descendant(cls, func):
        """
        Creates a subclass of this class that that uses `func` as
        :attr:`perform`. This allows class docs to vary depending on `func.
        """
        docs = 'Calls ":attr:`perform`"'
        return type(
            func.__name__,
            (cls, ),
            {'perform': func,
             '__doc__': docs})
