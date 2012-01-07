# -*- coding: utf-8 -*-

from chameleon import api

@api.register
def order_status(db, orderid, statusid):
    """
    Zmiana statusu zamówienia

    :param int orderid: Id zamówienia
    :param int statusid: Id statusu
    """

    cur = db.cursor()

    data = {}
    data['orderid'] = orderid
    data['statusid'] = statusid

    sql = """
            UPDATE `order`
            SET orderstatusid = %(statusid)s
            WHERE idorder = %(orderid)s
        """

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
