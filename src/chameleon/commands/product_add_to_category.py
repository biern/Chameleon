# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def product_add_to_category(db, productid, categoryid, userid=None):
    """
    Add product to category    

	:param int productid:
	:param int categoryid:
    :param int userid: 
	:return: Product category id
    """
    
    cur = db.cursor()
    sql = """
        INSERT INTO productcategory
        (
            productid, 
            categoryid, 
            addid
        )
        VALUES
        (
            %(productid)s, 
            %(categoryid)s, 
            %(addid)s
        )
        """
    data = {}
    data['productid'] = productid
    data['categoryid'] = categoryid
    data['addid'] = userid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
