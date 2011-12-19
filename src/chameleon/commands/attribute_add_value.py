# -*- coding: utf-8 -*-

from chameleon import api

@api.register
def attribute_add_value(db, name, propertyid, userid=None):
    """
    Create new product value (wartości)              
    :param str name:
    :param int propertyid:
    :param int userid:
	:return: Attribute value id
    """
        
    cur = db.cursor()
    
    sql = """
        INSERT INTO attributeproductvalue (
            idattributeproductvalue,
            attributeproductid, 
            name, 
            addid
        )
		VALUES
		(
		    NULL,
		    %(propertyid)s, 
		    %(name)s, 
		    %(userid)s 
		)
        """
    data = {}
    data['propertyid'] = propertyid
    data['name'] = name
    data['userid'] = userid
    
    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    valueid = cur.lastrowid
        
    return valueid