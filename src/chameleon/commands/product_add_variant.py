# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def product_add_variant(db, productid, type, value, stock, attribute_group_id, symbol, weight, status=1, userid=None):
    """
    Add variant to product

    :param int productid:
    :param int type: 1 - %, 2 +, 3 -, 4 =
    :param float value: Wartość modyfikatora
    :param int stock: Stan magazynowy
    :param int attribute_group_id: Id grupy cech
    :param str symbol: Symbol
    :param int status: Status (aktywny, nieaktywny)
    :param float weight: Waga
    :param int userid: Identyfikator użytkownika
    :return: Product variant id
    """

    cur = db.cursor()

    # Pobieramy wartośc ceny produktu
    cur.execute("""
                    SELECT
                        sellprice
                    FROM
                        product
                    WHERE
                        idproduct = %s
                """, (productid,)
                )

    priceBefore = cur.fetchone()

    if type == 1:
        price = float(priceBefore[0]) * (value/100)
    elif type == 2:
        price = float(priceBefore[0]) + value
    elif type == 3:
        price = float(priceBefore) - value
    elif type == 4:
        price = float(value)
    else:
        # @todo wyświetlić error
        pass

    sql = """
        INSERT INTO productattributeset
        (
            idproductattributeset,
            productid,
            suffixtypeid,
            value,
            addid,
            stock,
            attributegroupnameid,
            attributeprice,
            symbol,
            weight,
            status
        )
        VALUES
        (
            NULL,
            %(productid)s,
            %(type)s,
            %(value)s,
            %(userid)s,
            %(stock)s,
            %(attribute_group_id)s,
            %(price)s,
            %(symbol)s,
            %(weight)s,
            %(status)s
        )
        """
    data = {}
    data['productid'] = productid
    data['type'] = type
    data['value'] = value
    data['userid'] = userid
    data['stock'] = stock
    data['attribute_group_id'] = attribute_group_id
    data['price'] = price
    data['symbol'] = symbol
    data['weight'] = weight
    data['status'] = status

    cur.execute(sql, data)
    db.commit()

    return cur.lastrowid
