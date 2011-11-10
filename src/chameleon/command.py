# -*- coding: utf-8 -*-

from chameleon import utils


class DBCommandWrapper(object):
    def __call__(self, *args, **kwargs):
        """
        Calls :attr:`func`
        """
        self.perform(*args, **kwargs)

    def get_parser(self):
        return utils.parser_from_func(self.perform, skip=1)

    def shell_eval(self, argv):
        # TODO: Get default db
        parser = self.get_parser()
        args = parser.parse_args(argv)
        print(vars(args))

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
