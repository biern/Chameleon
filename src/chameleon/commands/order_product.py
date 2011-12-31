# -*- coding: utf-8 -*-

from chameleon import api

@api.register
def order_product(db, orderid, productid, productattributeid, qty):
    """
    Dodawanie produktu do nowego zamówienia

    :param int orderid:
    :param int productid:
    :param int productattributeid:
    :param int qty:
    """

    cur = db.cursor()

    name = ''
    price = 3
    qtyprice = 4
    vat = 3
    pricenetto = 5

    data = {}
    data['orderid'] = orderid
    data['productid'] = productid
    data['name'] = name
    data['price'] = price
    data['qty'] = qty
    data['qtyprice'] = qtyprice
    data['vat'] = vat
    data['pricenetto'] = pricenetto
    data['productattributeid'] = productattributeid

    sql = """
        INSERT INTO orderproduct SET
            orderid = %(orderid)s, 
            productid = %(productid)s,
            name = %(name)s,
            price = %(price)s,
            qty = %(qty)s,
            qtyprice = %(qtyprice)s,
            productattributesetid = %(productattributeid)s,
            vat = %(vat)s,
            pricenetto = %(pricenetto)s
        """

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    orderproductid = cur.lastrowid
    return orderproductid

 
