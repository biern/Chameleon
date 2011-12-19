# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def product_edit_basic_information(db, productid, name, url, enable, ean, delivelercode, producerid, languageid=None):
    """
    Edit product basic information
    :param int productid:
    :param str name:
    :param str url:
    :param int enable:
    :param str ean:
    :param str delivelercode:
    :param int producerid:
    :param int languageid:  
    """

    cur = db.cursor()
    sql = """
        UPDATE
		    producttranslation
		SET
			name = %(name)s, 
			seo = %(url)s
		WHERE
			productid = %(productid)s 
			AND languageid = %(languageid)s
        """
    data = {}
    data['name'] = name
    data['url'] = url
    data['productid'] = productid
    data['languageid'] = languageid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()  
    
    sql = """
        UPDATE
            product
		SET
			enable = %(enable)s, 
			ean = %(ean)s, 
			delivelercode = %(delivelercode)s, 
			producerid = %(producerid)s
		WHERE
			idproduct = %(idproduct)s
        """
    data = {}
    data['enable'] = enable
    data['ean'] = ean
    data['delivelercode'] = delivelercode
    data['producerid'] = producerid
    data['idproduct'] = productid
    
    cur = db.cursor()
    cur.execute(sql, data)
    db.commit() 