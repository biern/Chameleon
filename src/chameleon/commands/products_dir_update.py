# -*- coding: utf-8 -*-

import os

import chameleon
from chameleon import api


@api.register
def products_dir_update(db, root=".", *attributes):
    """
    Update products based on data stored in directries under root
    """
    dirs = [d for d in os.listdir(os.path.abspath(root))]
    dirs = [d for d in dirs if os.path.isdir(os.path.join(root, d)) and \
                d.isdigit()]
    for d in dirs:
        productid = int(d)
        d = os.path.join(root, d)
        attr_names = [a for a in os.listdir(d) if a in \
                     chameleon.commands.PRODUCT_UPDATE_ATTRS]
        attrs = {}
        for a in attr_names:
            attrs[a] = open(os.path.join(d, a)).read()

        print("Updating product {} with attrs: {}".format(
                productid, attrs))
