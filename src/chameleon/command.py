# -*- coding: utf-8 -*-

import inspect

from chameleon import utils
from chameleon.db import Database


class DBCommandWrapper(object):
    def __call__(self, db, *args, **kwargs):
        """
        Calls :attr:`perform` as an unbound function.
        """
        with db.conn:
            self.perform.im_func(db, *args, **kwargs)

    def get_parser(self):
        return utils.parser_from_func(self.perform, skip=1)

    def shell_eval(self, argv=None):
        parser = self.get_parser()
        args = parser.parse_args(argv)
        return self.call_from_namespace(Database(), args)

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
