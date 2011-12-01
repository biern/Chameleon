# -*- coding: utf-8 -*-

import csv
import os

from chameleon import api
from chameleon.commands import product_add


@api.register
def products_csv_import(db, path):
    """
    Imports products from csv file. Arguments for each product (row)
    are exactly the same as in :class:`product_add`.

    :param str path: Path to csv file.
    """
    # TODO: waits for product_add
    if not os.path.exists(path):
        print('File "{}" does not exist'.format(path))
        return

    reader = csv.reader(open(path, 'rb'))
    for i, row in enumerate(reader, 1):
        print('#{}: {} ...'.format(i, '; '.join(row)))
        try:
            # product_add(db, *row)
            pass
        except Exception, e:
            print("FAIL: {}".format(e))
            continue

        print("OK")
