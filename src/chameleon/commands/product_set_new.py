# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def product_set_new(db, productid, end, active=1, userid=None):
    """
    Set product as new
 
    :param int productid: Id produktu
    :param string end: Data zakończenia nowości
    :param int active: Czy aktywować nowość
    :param int userid: Id administratora
    """

    cur = db.cursor()
    sql = """
            INSERT INTO productnew
            (
                idproductnew,
                productid,
                enddate,
                addid,
                active
            )
            VALUES
            (
                NULL,
                %(productid)s,
                %(end)s,
                %(userid)s,
                %(active)s
            )
          """

    data = {}
    data['productid'] = productid
    data['end'] = end
    data['userid'] = userid
    data['active'] = active

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

