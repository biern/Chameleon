# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def product_promotion(db, productid, price, start, end, active=1):
    """
    Set promotion for product
    
    :param int active: Czy aktywować promocje
    :param int productid: Id produktu
    :param float price: Cena zniżki
    :param string start: Data startu zniżki
    :param string end: Data zakończenia zniżki
    """

    cur = db.cursor()
    sql = """
        UPDATE product SET
            discountprice = %(price)s,
            promotionstart = %(start)s,
            promotionend = %(end)s,
            promotion = %(active)s
        WHERE
            idproduct = %(productid)s
        """
    data = {}
    data['price'] = price
    data['start'] = start
    data['end'] = end
    data['productid'] = productid
    data['active'] = active

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
