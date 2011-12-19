# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def producer_add(db, name, www, description,
                 producerid=0, photoid=1,
                 keyword_title='', keyword='', keyword_description='',
                 languageid=None, userid=None):
    """
    Add producer or translation

    :param int producerid: If greater than 0, add only translation
    :param str name: Name (required, language_unique)
    :param str www: WWW address
    :param str email: Email (required, email)
    :param str keyword_title: Keyword title
    :param str keyword: Keywords
    :param str keyword_description: Keywords description
    :param int photoid:
    :param int languageid:
    :param int userid:
    :return: Added / updated producer id
    """
    db.validate('name', name,
                'required',
                ('language_unique',
                 {'table': 'producertranslation', 'column': 'name'}))

    if producerid == 0:
        sql = """
        INSERT INTO producer (addid, photoid) VALUES (%(addid)s,
        %(photoid)s)"""

        data = {}
        data['photoid'] = photoid
        data['addid'] = userid

        cur = db.cursor()
        cur.execute(sql, data)
        db.commit()

        producerid = cur.lastrowid

    sql = """INSERT INTO producertranslation (
               producerid,
               name,
               seo,
               description,
               keyword_title,
               keyword,
               keyword_description,
               languageid
          )
          VALUES
          (
               %(producerid)s,
               %(name)s,
               %(seo)s,
               %(description)s,
               %(keyword_title)s,
               %(keyword)s,
               %(keyword_description)s,
               %(languageid)s
          )"""

    data = {}
    data['producerid'] = producerid
    data['name'] = name
    data['seo'] = www
    data['description'] = description
    data['keyword_title'] = keyword_title
    data['keyword'] = keyword
    data['keyword_description'] = keyword_description
    data['languageid'] = languageid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    return producerid
