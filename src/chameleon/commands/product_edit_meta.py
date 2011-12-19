# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def product_edit_meta(db, productid, keyword_title, keyword, keyword_description):
    """
    Edit product meta information

	:param int productId:
    :param str keyword_title: Keyword title
    :param str keyword: Keywords 
    :param str keyword_description: Keywords description
    """
    
    cur = db.cursor()
    sql = """
        UPDATE
            producttranslation
		SET
			keyword_title = %(keyword_title)s, 
			keyword = %(keyword)s, 
			keyword_description = %(keyword_description)s
		WHERE
			productid = %(productid)s
        """
    data = {}
    data['keyword_title'] = keyword_title
    data['keyword'] = keyword
    data['keyword_description'] = keyword_description
    data['productid'] = productid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
