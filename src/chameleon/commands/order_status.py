# -*- coding: utf-8 -*-

from chameleon import api

@api.register
def order_status(db, orderid, statusid, comment, userid=None):
    """
    Zmiana statusu zamówienia

    :param int orderid: Id zamówienia
    :param int statusid: Id statusu
    :param str comment: Komentarz do zmiany statusu
    :param int userid: Id administratora
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


    cur = db.cursor()

    data = {}
    data['comment'] = comment
    data['userid'] = userid
    data['statusid'] = statusid
    data['orderid'] = orderid

    sql = """
            INSERT INTO orderhistory
            (
                idorderhistory,
                `content`,
                addid,
                orderstatusid,
                orderid
            )
            VALUES
            (
                NULL,
                %(comment)s,
                %(userid)s,
                %(statusid)s,
                %(orderid)s
            )
          """

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

