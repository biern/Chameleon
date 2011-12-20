# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def producer_add(db, name, www, description,
                 producerid=0, photoid=1,
                 keyword_title='', keyword='', keyword_description='',
                 languageid=None, userid=None, shopid=None):
    """
    Add producer or translation

    :param int producerid: If greater than 0, add only translation
    :param str name: Nazwa
    :param str www: Adres URL
    :param str description: Opis 
    :param str keyword_title: Meta tytuł
    :param str keyword: Słowa kluczowe
    :param str keyword_description: Meta opis
    :param int photoid: Id zdjęcia
    :param int languageid: Id języka
    :param int userid: Id użytkownika
    :param int shopid: Id sklepu
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
    
    sql = """INSERT INTO producerview (
               idproducerview,
               producerid,
               viewid,
               addid
          )
          VALUES
          (    
               NULL,
               %(producerid)s,
               %(shopid)s,
               %(userid)s
          )"""

    data = {}
    data['producerid'] = producerid
    data['shopid'] = shopid
    data['userid'] = userid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    return producerid
