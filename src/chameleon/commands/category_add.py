# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def category_add(db, name, www, short_description = '', description = '',
                 keyword_title = '', keyword = '', keyword_description = '',
                 distinction = 1, enable = 1, languageid=None, userid=None):
    """
    Add category     

    :param str name: 
    :param str www:
    :param str short_description:
    :param str description:
    :param str keyword_title:
    :param str keyword: 
    :param str keywordDescription:
    :param int distinction:
    :param int enable:
    :param int languageid:
    :param int userid:
    :return: Category Id
    """
    
    cur = db.cursor()

    sql = """
            INSERT INTO category
            (
                categoryid, 
                addid, 
                distinction, 
                enable
            )
            VALUES
            (
                NULL, 
                %(addid)s, 
                %(distinction)s, 
                %(enable)s
            )
        """
    data = {}
    data['addid'] = userid
    data['distinction'] = distinction
    data['enable'] = enable

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
    
    categoryid = cur.lastrowid 
    
    sql = """
            INSERT INTO categorytranslation
    		(
    		    categoryid,
    		    name,
    		    shortdescription, 
    		    description, 
    		    languageid, 
    		    seo, 
    		    keyword_title, 
    		    keyword, 
    		    keyword_description
		    )
			VALUES
			(
			    %(categoryid)s,
			    %(name)s,
			    %(short_description)s, 
			    %(description)s, 
			    %(languageid)s, 
			    %(seo)s, 
			    %(keyword_title)s, 
			    %(keyword)s, 
			    %(keyword_description)s
		    )
        """
    data = {}
    data['categoryid'] = categoryid
    data['name'] = name
    data['short_description'] = short_description
    data['description'] = description
    data['languageid'] = languageid
    data['seo'] = www
    data['keyword_title'] = keyword_title
    data['keyword'] = keyword
    data['keyword_description'] = keyword_description
    
    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()
    
    return categoryid 

