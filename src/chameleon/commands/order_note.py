# -*- coding: utf-8 -*-

from chameleon import api

@api.register
def order_note(db, orderid, comment, userid=None):
    """
    Dodanie notatki na temat zamówienia

    :param int orderid: Id zamówienia
    :param str comment: Treść notatki
    :param int userid: Id administratora
    """

    cur = db.cursor()

    data = {}
    data['comment'] = comment
    data['orderid'] = orderid
    data['userid'] = userid

    sql = """
            INSERT INTO `ordernotes`
            (
                idordernotes,
                `content`,
                orderid,
                addid
            )
            VALUES
            (
                NULL,
                %(comment)s,
                %(orderid)s,
                %(userid)s
            )
        """

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
