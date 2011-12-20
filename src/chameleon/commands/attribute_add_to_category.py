# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def attribute_add_to_category(db, groupid, propertyid, categoryid,
                              userid=None):
    """
    Add attribute group and attribute property to category
    :param int groupid:
    :param int propertyid:
    :param int categoryid:
    :param int userid:
    :return: Attribute product id
    """

    cur = db.cursor()

    sql = """
        INSERT INTO categoryattributeproduct (
            idcategoryattributeproduct,
            categoryid,
            attributeproductid,
            addid,
            attributegroupnameid
        )
        VALUES
        (
            NULL,
            %(categoryid)s,
            %(propertyid)s,
            %(userid)s,
            %(groupid)s
        )
        """
    data = {}
    data['categoryid'] = categoryid
    data['propertyid'] = propertyid
    data['groupid'] = groupid
    data['userid'] = userid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
