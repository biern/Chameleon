# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def attribute_add_property(db, groupid, name, propertyid=0, userid=None):
    """
    Create new product property (cechy)

    :param int groupid:
    :param str name:
    :param int propertyid:
    :param int userid:
    :return: Attribute product id
    """

    cur = db.cursor()

    if propertyid == 0:
        sql = """
            INSERT INTO attributeproduct (
                idattributeproduct,
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

        propertyid = cur.lastrowid

    sql = """
        INSERT INTO attributegroup (
            idattributegroup,
            attributegroupnameid,
            attributeproductid,
            addid
        )
		VALUES
		(
		    NULL,
		    %(groupid)s,
		    %(propertyid)s,
		    %(userid)s
		)
        """
    data = {}
    data['groupid'] = groupid
    data['propertyid'] = propertyid
    data['userid'] = userid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    return propertyid
