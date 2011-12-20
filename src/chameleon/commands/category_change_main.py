# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def category_change_main(db, categoryid, maincategoryid):
    """
    Change main category to given category

    :param int categoryid:
    :param int maincategoryid:
    """

    cur = db.cursor()

    sql = """
            UPDATE
                category
            SET
                categoryid = %(maincategoryid)s
            WHERE
                idcategory = %(categoryid)s
        """

    data = {}
    data['maincategoryid'] = maincategoryid
    data['categoryid'] = categoryid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
