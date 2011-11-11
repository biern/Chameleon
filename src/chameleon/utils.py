# -*- coding: utf-8 -*-

import argparse
import inspect
import os
import re
import sys


def dict_from_module(path):
    """
    Returns public module variables as a dict. If module was not found,
    None is returned.

    :param str path: Filesystem path to module, without '.py' at the end.
    """
    res = {}

    directory, name = os.path.split(path)
    # Solves problems of not being in package
    sys.path.insert(0, os.path.abspath(directory))
    try:
        module = __import__(name)
    except ImportError:
        return None
    finally:
        sys.path = sys.path[1:]

    for name in dir(module):
        if name.startswith('_'):
            continue

        res[name] = getattr(module, name)

    return res


def add_subparsers(subparser, parsers_with_names):
    for name, sub in parsers_with_names:
        sub_copy = subparser.add_parser(
            name, description=sub.description)

        for action in sub._actions:
            if action.option_strings and \
                    action.option_strings[1] == '--help':
                continue

            sub_copy._add_action(action)


def parser_from_func(func, skip=0, parser=None):
    """
    Creates argparse.parser based on given func args.

    Information about arguments is extracted from function definition and
    docstrings written in sphinx format (if available).

    :param func: Func to parse args for
    :param int skip: Skip first ``n`` arguments (ie. use to ommit 'self')
    """
    # Extracting data from method arguments
    args, varargs, keywords, defaults = inspect.getargspec(func)

    # ommiting 'self'
    args = args[skip:]

    # Extracting data from docstring
    doc = inspect.getdoc(func) or ""
    docs_data = {}
    for match in re.finditer(
        r':param (?P<type>\w+) (?P<name>[\w_]+): (?P<help>.*)\s*',
        doc):
        d = match.groupdict()
        docs_data[d['name']] = {'type': eval(d['type']),
                                'help': d['help']}

    defaults = defaults or tuple()

    # Creating parser
    description = "{}: {}".format(
        func.__name__,
        doc.split("\n\n")[0])
    parser = argparse.ArgumentParser(description=description)

    # Adding arguments
    for i, arg in enumerate(args):
        kwargs = {}
        kwargs.update(docs_data.get(arg, {}))

        # Default arg
        default = None
        default_index = i - len(args) + len(defaults)
        if default_index >= 0:
            default = kwargs['default'] = defaults[default_index]
            kwargs['help'] = "{} (default: {})".format(
                kwargs.get('help', ''), default)

        # Name + optional arg or not
        flags = ['--{}'.format(arg) if default else arg]

        parser.add_argument(*flags, **kwargs)

    if varargs:
        parser.add_argument(varargs, nargs='*')

    return parser
