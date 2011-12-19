# -*- coding: utf-8 -*-

from chameleon import api

@api.register
def attribute_add_group(db, name, userid=None):
    """
    Create new attribute group
    :param str name:
    :param int userid:
	:return: Attribute group id
    """
        
    cur = db.cursor()
    sql = """
        INSERT INTO attributegroupname (
            idattributegroupname, 
            name, 
            addid
        )
		VALUES
		(
		    NULL, 
		    %(name)s, 
		    %(userid)s 
		)
        """
    data = {}
    data['name'] = name
    data['userid'] = userid
        
    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
    
    attributeGroupId = cur.lastrowid
    
    return attributeGroupId