# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def product_similar(db, productid, relatedproductid, userid=None):
    """
    Set similar products
 
    :param int productid: Id produktu
    :param int relatedproductid: Id powiązanego produktu
    :param int userid: Id administratora
    """

    cur = db.cursor()
    sql = """
            INSERT INTO similarproduct
            (
                idsimilarproduct,
                productid,
                relatedproductid,
                addid
            )
            VALUES
            (
                NULL,
                %(productid)s,
                %(relatedproductid)s,
                %(userid)s
            )
          """

    data = {}
    data['productid'] = productid
    data['relatedproductid'] = relatedproductid
    data['userid'] = userid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    # I na odwrót też podajemy
    data = {}
    data['productid'] = relatedproductid
    data['relatedproductid'] = productid
    data['userid'] = userid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()




