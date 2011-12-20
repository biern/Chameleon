# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def variant_add_value(db, variantid, attributevalueid, userid=None):
    """
    Add value do variant    

	:param int variantid:
	:param int attributevalueid:
    """
    
    cur = db.cursor() 
        
    sql = """
        INSERT INTO productattributevalueset
        (   
            idproductattributevalueset,
            attributeproductvalueid,
            productattributesetid,
            addid
        )
        VALUES
        (  
            NULL,
            %(variantid)s,
            %(attributevalueid)s,
            %(userid)s          
        )
        """
    data = {}
    data['variantid'] = variantid
    data['attributevalueid'] = attributevalueid
    data['userid'] = userid
    
    cur.execute(sql, data)
    db.commit() 
