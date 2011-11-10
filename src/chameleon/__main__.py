# -*- coding: utf-8 -*-

import argparse

from chameleon import api, utils


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='chameleon',
        description="Chameleon command line API")
    utils.add_subparsers(parser, [(k, v.get_parser()) for k, v in api.items()])
    parser.parse_args()
