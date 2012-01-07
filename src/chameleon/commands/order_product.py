# -*- coding: utf-8 -*-

from chameleon import api

@api.register
def order_product(db, orderid, productid, qty, productattributeid=None, languageid=None):
    """
    Dodawanie produktu do nowego zamówienia

    :param int orderid: Id zamówienia
    :param int productid: Id produktu
    :param int qty: Ilość produktu
    :param int productattributeid: Id atrybuty produktu
    :param int languageid: Id języka
    """

    cur = db.cursor()

    # Get info about product
    data = {}
    data['productid'] = productid
    data['languageid'] = languageid

    sql = """
            SELECT
                p.sellprice,
                v.value,
                t.name
            FROM
                product as p
            INNER JOIN
                vat as v
            ON
                p.vatid = v.idvat
            INNER JOIN
                producttranslation as t
            ON
                p.idproduct = t.productid
                AND t.languageid = %(languageid)s
            WHERE
                p.idproduct = %(productid)s
        """
    
    cur.execute(sql, data)
    product = cur.fetchone()

    if product is None:
        raise IOError('This product not exist')

    priceSql = product[0]

    # Jeżeli użytkownik podał wariant, zmieniamy cene netto
    if productattributeid is not None:
        cur.execute(
        """
            SELECT
                attributeprice
            FROM
                productattributeset
            WHERE
                idproductattributeset = %s
        """, (productattributeid))
    
        priceSql = cur.fetchone()[0]

        # Musimy też stworzyć dodatkowe info na temat wariantu
        
        # Pobieramy nazwę atrubutu
        cur.execute(
            """
                SELECT
                    d.name,
                    e.name as b
                FROM
                    productattributevalueset as c
                INNER JOIN
                    attributeproductvalue as d
                ON
                    c.attributeproductvalueid = d.idattributeproductvalue
                INNER JOIN
                    attributeproduct as e
                ON
                    d.attributeproductid = e.idattributeproduct
                WHERE
                    c.productattributesetid = %s

            """, (productattributeid))

        atributeArray = cur.fetchone()[0] 

    name = product[2]
    price = priceSql*((product[1]+100)/100) # kwota brutto jednego produktu
    qtyprice = qty*price #qty * kwota brutto
    vat = (product[1]/100)*priceSql # kwota vat z jednego produktu
    pricenetto = priceSql # kwota netto jednego produktu 

    data = {}
    data['orderid'] = orderid
    data['productid'] = productid
    data['name'] = name
    data['price'] = price
    data['qty'] = qty
    data['qtyprice'] = qtyprice
    data['vat'] = vat
    data['pricenetto'] = pricenetto
    data['productattributeid'] = productattributeid

    sql = """
        INSERT INTO orderproduct SET
            orderid = %(orderid)s, 
            productid = %(productid)s,
            name = %(name)s,
            price = %(price)s,
            qty = %(qty)s,
            qtyprice = %(qtyprice)s,
            productattributesetid = %(productattributeid)s,
            vat = %(vat)s,
            pricenetto = %(pricenetto)s
        """

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    orderproductid = cur.lastrowid

    if productattributeid is not None:
        data = {}
        data['attributeName'] = atributeArray[0]
        data['attributeGroup'] = atributeArray[1]
        data['orderproductid'] = orderproductid

        # Dodajemy nazwę i typ atrybutu do tabeli łączącej
        sql = """
            INSERT INTO orderproductattribute
            (
                idorderproductattribute,
                `name`,
                `group`,
                orderproductid
            )
            VALUES
            (
                NULL,
                %(attributeName)s,
                %(attributeGroup)s,
                %(orderproductid)s
            )
            """

        cur = db.cursor()
        cur.execute(sql, data)
        db.commit()


    # Musimy pobrać id wysyłki bieżącego zamówienia
    cur = db.cursor()
    cur.execute(
        """
            SELECT
                dispatchmethodid
            FROM
                `order`
            WHERE
                `idorder` = %s
        """, (orderid))

    dispatchid = cur.fetchone()[0]

    # Musimy pobrać bieżąca cene zamówienia
    sql = """
        UPDATE `order` SET  
            price = price + %(qtyprice)s 
        WHERE
            idorder = %(orderid)s
    """

    data = {}
    data['qtyprice'] = qtyprice
    data['orderid'] = orderid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    cur.execute(
    """
        SELECT
            price    
        FROM
            `order`   
        WHERE
            idorder = %s
    """, (orderid))

    currentPrice = cur.fetchone()[0]

    # Pobieramy bieżącą cene wysyłki
    cur.execute(
    """
        SELECT
            dispatchmethodcost,
            vat
        FROM
            dispatchmethodprice
        WHERE
            dispatchmethodid = %s
            AND %s >= `from`
            AND %s <= `to`
    """, (dispatchid, currentPrice, currentPrice))

    dispatchArray = cur.fetchone()
    dispatchCost = dispatchArray[0]
    dispatchVat = dispatchArray[1]

    if dispatchCost is None:
        raise IOError('Dispatch method cost not exist for this price')

    # Musimy sprawdzić czy trzeba doliczyć vat do przesyłki
    if dispatchVat is not None:
            cur.execute(
                """
                    SELECT
                        value
                    FROM
                        vat
                    WHERE
                        idvat = %s
                """, (dispatchVat))

            dispatchCost = dispatchCost*(cur.fetchone()[0]/100+1)
    

    # Musimy zupdatować dane w tabeli order, gdyż dodaliśmy nowy produkt
    sql = """
        UPDATE `order` SET  
            dispatchmethodprice = %(dispatchCost)s,
            globalprice = price + dispatchmethodprice
        WHERE
            idorder = %(orderid)s
        """

    data = {}
    data['dispatchCost'] = dispatchCost
    data['orderid'] = orderid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()


    return orderproductid
