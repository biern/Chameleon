# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def product_add_image(db, productid, imageid, ismain=0, userid=None):
    """
    Add product to image
    :param int productid:
    :param int imageid:
    :param int ismain:
    """

    cur = db.cursor()
    sql = """
        DELETE FROM productphoto
        WHERE
            productid = %(productid)s
            AND photoid = %(imageid)s
        """
    data = {}
    data['productid'] = productid
    data['imageid'] = imageid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    if ismain == 1:
        sql = """
            UPDATE productphoto
            SET
                mainphoto = 0
            WHERE
                productid = %(productid)s
            """
        data = {}
        data['productid'] = productid

        cur = db.cursor()
        cur.execute(sql, data)
        db.commit()

    sql = """
        INSERT INTO productphoto (
            idproductphoto,
            productid,
            photoid,
            addid,
            mainphoto
        )
        VALUES
        (
            NULL,
            %(productid)s,
            %(imageid)s,
            %(userid)s,
            %(ismain)s
        )
        """
    data = {}
    data['productid'] = productid
    data['imageid'] = imageid
    data['userid'] = userid
    data['ismain'] = ismain

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
