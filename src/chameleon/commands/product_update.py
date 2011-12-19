# -*- coding: utf-8 -*-

from chameleon import api


PRODUCT_UPDATE_ATTRS = ['value', 'title', 'stock']


@api.register
def product_update(db, productid, attr, value):
    """
    Update product column

    :param str attr: Attribute name
    :param value: Attribute value
    """
    # STUB - definicja jest w porządku, reszta to szkic

    if attr not in PRODUCT_UPDATE_ATTRS:
        print('Attribute name must be one of: "{}"'.format(",".join(attr)))
        return

    if attr == "title":
        # bla bla bla
        return

    if attr in ('value', 'stock'):
        sql = """bla bla bla"""
        data = {attr: value}
        cur = db.cursor()
        cur.execute(sql, data)
        db.commit()
