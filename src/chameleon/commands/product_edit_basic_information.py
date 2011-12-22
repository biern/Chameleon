# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def product_edit_basic_information(db, productid, enable, ean,
                                   delivelercode, producerid, delivererid,
                                   languageid=None, userid=None):
    """
    Edit product basic information

    :param int productid: Id produktu
    :param int enable: Wyświetl produkt w sklepie
    :param str ean: Kod EAN
    :param str delivelercode: Kod dostawcy
    :param int producerid: ID producenta
    :param int delivererid: Id dostawcy
    :param int languageid:
    """

    cur = db.cursor()

    sql = """
        UPDATE
            product
        SET
            enable = %(enable)s,
            ean = %(ean)s,
            delivelercode = %(delivelercode)s,
            producerid = %(producerid)s
        WHERE
            idproduct = %(idproduct)s
        """
    data = {}
    data['enable'] = enable
    data['ean'] = ean
    data['delivelercode'] = delivelercode
    data['producerid'] = producerid
    data['idproduct'] = productid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    sql = """
        INSERT INTO productdeliverer (
            idproductdeliverer,
            productid,
            delivererid,
            addid
        )
        VALUES
        (
            NULL,
            %(productid)s,
            %(delivererid)s,
            %(userid)s
        )
        """
    data = {}
    data['productid'] = productid
    data['delivererid'] = delivererid
    data['userid'] = userid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
