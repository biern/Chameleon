# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def product_edit_stock(db, productid, stock, track_stock, shipping_cost):
    """
    Edit stock info    

    :param int productid:
	:param int stock:
	:param boolean track_stock:
	:param float shipping_cost:
    """
    
    cur = db.cursor()
    sql = """
        UPDATE 
            product 
        SET
            stock = %(stock)s, 
            trackstock = %(track_stock)s, 
            shippingcost = %(shipping_cost)s 
        WHERE
            idproduct = %(productid)s
        """
    data = {}
    data['stock'] = stock
    data['track_stock'] = track_stock
    data['shipping_cost'] = shipping_cost
    data['productid'] = productid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
