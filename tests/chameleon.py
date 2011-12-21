#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

import logging

logging.basicConfig(level=logging.DEBUG)

from chameleon import shell_eval


if __name__ == "__main__":
    shell_eval()
