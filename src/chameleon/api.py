# -*- coding: utf-8 -*-
from chameleon.command import DBCommandWrapper


class Library(dict):
    def register(self, func):
        wrapper = DBCommandWrapper.for_func(func)
        self[func.__name__] = wrapper
        return wrapper

api = Library()
"""
Holds all API functions.
"""
