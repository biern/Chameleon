# -*- coding: utf-8 -*-

from chameleon import api


PRODUCT_UPDATE_ATTRS = ['value', 'title']


@api.register
def product_update(db, productid, attr, value):
    """
    Update product column

    :param str attr: Attribute name
    :param value: Attribute value
    """
    # STUB - definicja jest w porządku, reszta to szkic
    if attr == "title":
        # bla bla bla
        return

    if attr in ('value', 'stock'):
        sql = """bla bla bla"""
        data = {attr: value}
        cur = db.cursor()
        cur.execute(sql, data)
        db.commit()
