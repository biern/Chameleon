# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def deliverer_add(db, name, www, email,
                  photoid=1, delivererid=0,
                  userid=None, languageid=None):
    """
    Add deliverer or translation

    :param int delivererid: If greater than 0, add only translation
    :param str name: Name (required, language_unique)
    :param str www: www address
    :param str email: Email (required, email)
    :param int photoid:
    :return: Added / updated deliverer id
    """
    db.validate('name', name, 'required',
                ('language_unique',
                 {'table': 'deliverertranslation', 'column': 'name'}))
    db.validate('email', email, 'required', 'email')
    db.validate('languageid', languageid, 'required')

    if delivererid == 0:
        sql = """
        INSERT INTO deliverer (photoid, addid)
        VALUES (%(photoid)s, %(addid)s)"""
        data = {}
        data['photoid'] = photoid
        data['addid'] = userid

        cur = db.cursor()
        cur.execute(sql, data)
        db.commit()
        delivererid = cur.lastrowid

    sql = """
    INSERT INTO deliverertranslation (delivererid, name, www, email, languageid)
    VALUES (%(delivererid)s, %(name)s, %(www)s, %(email)s, %(languageid)s)
    """

    data = {}
    data['delivererid'] = delivererid
    data['name'] = name
    data['www'] = www
    data['email'] = email
    data['languageid'] = languageid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    return delivererid
