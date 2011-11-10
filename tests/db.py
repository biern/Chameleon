# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

from chameleon.db import Database


db = Database()
db.connect()
