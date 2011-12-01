# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

from chameleon.commands import products_csv_import
from chameleon.db import Database


if __name__ == "__main__":
    products_csv_import(Database(), "products.csv")
