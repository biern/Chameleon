# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def product_add(db, name, url, stock, vatid, buyprice, sellprice, weight,
                languageid=None, userid=None):
    """
    Add product
    :param str name:
    :param str url:
    :param int stock:
    :param int vatiId:
    :param float buyprice:
    :param float sellprice:
    :param float weight:
    :param int languageid:
    :param int userid:
    :return: Product id
    """

    cur = db.cursor()
    sql = """
        INSERT INTO product (
            idproduct,
            stock,
            vatid,
            buyprice,
            sellprice,
            weight,
            addid
        )
        VALUES
        (
            NULL,
            %(stock)s,
            %(vatid)s,
            %(buyprice)s,
            %(sellprice)s,
            %(weight)s,
            %(addid)s
        )
        """
    data = {}
    data['stock'] = stock
    data['vatid'] = vatid
    data['buyprice'] = buyprice
    data['sellprice'] = sellprice
    data['weight'] = weight
    data['addid'] = userid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    productid = cur.lastrowid

    sql = """
        INSERT INTO producttranslation (
            productid,
            name,
            seo,
            languageid
        )
        VALUES
        (
            %(productid)s,
            %(name)s,
            %(url)s,
            %(languageid)s
        )
        """
    data = {}
    data['productid'] = productid
    data['name'] = name
    data['url'] = url
    data['languageid'] = languageid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    sql = """
        INSERT INTO productsearch (
            productid,
            languageid,
            name
        )
        VALUES
        (
            %(productid)s,
            %(languageid)s,
            %(name)s
        )
        """
    data = {}
    data['productid'] = productid
    data['languageid'] = languageid
    data['name'] = name

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    return productid
