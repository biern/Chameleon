# -*- coding: utf-8 -*-

from chameleon import api
from phpserialize import unserialize, serialize
from random import choice
import string


@api.register
def order_create(db, dispatchid, paymentid, customeropinion, userid=None, shopid=None, encryption_key=None, languageid=None):
    """
    Tworzenie nowego zamówienia

    :param int dispatchid: Identyfikator sposobu wysyłki
    :param int paymentid: Identyfikator płatności
    :param str customeropinion: Opinia klienta
    :param int userid:
    :param int shopid:
    :param str encryption_key:
    """

    cur = db.cursor()

    # Pobieramy nazwę wysyłki

    cur.execute(
        """
        SELECT
            name
        FROM
            dispatchmethod
        WHERE
            iddispatchmethod = %s
        """, (dispatchid))

    dispatchName = cur.fetchone()[0]

    if dispatchName is None:
        raise IOError('Unsuporrted dispatch id')

    # Pobieramy nazwę płątności

    cur.execute(
        """
        SELECT
            name
        FROM
            paymentmethod
        WHERE
            idpaymentmethod = %s
        """, (paymentid))

    paymentName = cur.fetchone()[0]

    if paymentName is None:
        raise IOError('Unsuporrted payment id')

    price = 0 # Tymczasowa zmienna ceny

    # Metoda poszukiwania ceny wysyłki względem ceny zakupu
    cur.execute(
        """
        SELECT
            dispatchmethodcost
        FROM
            dispatchmethodprice
        WHERE
            dispatchmethodid = %s
            AND `from` >= %s
            AND `to` <= %s
        """, (dispatchid, price, price))

    dispatchCost = cur.fetchone()[0]

    if dispatchCost is None:
        raise IOError('Dispatch method cost not exist for this price')

    # Standardowo, szukamy waluty PLN
    currencyName = "PLN"

    cur.execute(
        """
        SELECT
            idcurrency
        FROM
            currency
        WHERE
            currencysymbol = %s
        """, (currencyName))

    currencyId = cur.fetchone()[0]

    if dispatchCost is None:
        raise IOError('Dispatch method cost not exist for this price')


    # Musimy wygenerować losowy id sesji
    def GenPasswd2(length=8, chars=string.letters + string.digits):
        return ''.join([choice(chars) for i in range(length)])
    
    sessionId = GenPasswd2(8,string.digits) + GenPasswd2(15,string.ascii_letters)

    globalPrice = price+dispatchCost
    
    orderStatus = 6 # status zamówienia 
    
    data = {}
    data['dispatchCost'] = dispatchCost
    data['globalPrice'] = globalPrice
    data['orderStatus'] = orderStatus
    data['dispatchName'] = dispatchName
    data['paymentName'] = paymentName
    data['dispatchid'] = dispatchid
    data['paymentid'] = paymentid
    data['userid'] = userid
    data['customeropinion'] = customeropinion
    data['currencyId'] = currencyId
    data['currencyName'] = currencyName
    data['sessionId'] = sessionId
    data['shopid'] = shopid

    sql = """
        INSERT INTO `order` (
            idorder,
            price,
            dispatchmethodprice, -- Koszty wysyłki
            globalprice, -- Cena globalna
            orderstatusid,
            dispatchmethodname, -- Nazwa wysyłki
            paymentmethodname, -- Nazwa płatności
            dispatchmethodid,
            paymentmethodid,
            addid,
            customeropinion, -- Opinia klienta
            currencyid,
            currencysymbol,
            sessionid,
            viewid,
            globalqty,
            globalpricenetto
        )
        VALUES
        (
            NULL,
            0, -- Na razie cene ustawiam na zero
            %(dispatchCost)s,
            %(globalPrice)s,
            %(orderStatus)s,
            %(dispatchName)s,
            %(paymentName)s,
            %(dispatchid)s,
            %(paymentid)s,
            %(userid)s,
            %(customeropinion)s,
            %(currencyId)s,
            %(currencyName)s,
            %(sessionId)s,
            %(shopid)s,
            0,
            0
        )
        """
    
    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    orderid = cur.lastrowid
    return orderStatus
