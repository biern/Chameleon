# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def add_product(db, title, stock, value, unit=1):
    """
    Some docs

    :param str title: Nazwa produktu
    :param int stock: Liczba w magazynie
    :param float value: Cena
    """
    cur = db.cursor()

    query = """
        INSERT INTO product SET
        producerid =NULL,
        stock=%(stock)s,
        trackstock=0,
        shippingcost=0,
        enable=1,
        weight=1,
        width=NULL,
        height=NULL,
        deepth=NULL,
        unit=%(unit)s,
        vatid=3,
        ean='',
        delivelercode='',
        buyprice=0,
        sellprice=0,
        buycurrencyid = 28,
        sellcurrencyid = 28,
        addid=1,
        technicaldatasetid=NULL,
        promotion = 0,
        discountprice = 0,
        promotionstart = NULL,
        promotionend = NULL
        """
    cur.execute(query, dict(
            stock=stock,
            unit=unit))

    # # Przykład bez mapowania nazw:
    # query = """
    #     INSERT INTO product SET
    #     producerid =NULL,
    #     stock=%s,
    #     unit=%s,
    #     (...)
    #     """
    # cur.execute(query, (stock, unit))


    # Tu coś nie bangla
    # query = """
    #     INSERT INTO producttranslation
    #         (productid, name, shortdescription,longdescription,
    #          description, languageid, seo, keyword_title, keyword,
    #          keyword_description)
    #     VALUES (1, %(title)s, '','', '', 1, %(title)s, '', '', '')
    # """
    # cur.execute(query, dict(
    #         title=title))

    # I tak potrzeba jeszcze kilka zapytań dopisać (przykłdowy log z
    # dodawania produktu jest w db_logs)
    db.commit()
