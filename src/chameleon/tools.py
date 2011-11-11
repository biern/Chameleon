# -*- coding: utf-8 -*-

import argparse

from chameleon import Database, api, utils


def shell_eval(argv=None):
    parser = argparse.ArgumentParser(
        prog='chameleon',
        description="Chameleon command line API")
    utils.add_subparsers(parser, [(k, v.get_parser()) for k, v in api.items()])
    args = parser.parse_args(argv)
    func = api[args.subparser]
    kwargs = vars(args)
    kwargs.pop('subparser')
    kwargs.pop('args')
    print kwargs
    func(Database(), **kwargs)
