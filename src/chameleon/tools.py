# -*- coding: utf-8 -*-

import argparse

from chameleon import Database, api, utils


def shell_eval(argv=None):
    parser = argparse.ArgumentParser(
        prog='chameleon',
        description="Chameleon command line API")
    utils.add_subparsers(
        parser.add_subparsers(dest='subparser'),
        [(k, v.get_parser()) for k, v in api.items()])
    args = parser.parse_args(argv)
    func = api[args.subparser]
    f_args = func.args_from_namespace(args)
    func(Database(), *f_args)
