# -*- coding: utf-8 -*-

import argparse

from chameleon import Database, api, utils


def shell_eval(argv=None):
    db = Database()
    parser = argparse.ArgumentParser(
        prog='chameleon',
        description="Chameleon command line API")
    utils.add_subparsers(
        parser.add_subparsers(dest='subparser'),
        [(k, v.get_parser(db)) for k, v in api.items()])
    args = parser.parse_args(argv)
    func = api[args.subparser]
    value = func.call_from_namespace(db, args)
    if value is not None:
        print(value)
