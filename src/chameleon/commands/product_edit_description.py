# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def product_edit_description(db, productid, shortdescription, description, longdescription,
                            languageid=None, userid=None):
    """
    Edit product description
    :param int productid: Id produktu
    :param str shortdescription: Krótki opis
    :param str description: Długi opis
    :param str longdescription: Dodatkowe informacje
    :param int languageid: Id języka
    :param int userid: Id użytkownika
    """

    cur = db.cursor()

    sql = """
        UPDATE
            producttranslation
        SET
            shortdescription = %(shortdescription)s,
            description = %(description)s,
            longdescription = %(longdescription)s
        WHERE
            productid = %(productid)s
            AND languageid = %(languageid)s
        """
        
    data = {}
    data['shortdescription'] = shortdescription
    data['description'] = description
    data['longdescription'] = longdescription
    data['productid'] = productid
    data['languageid'] = languageid    

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
