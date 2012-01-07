# -*- coding: utf-8 -*-

from chameleon import api

@api.register
def order_client(db, orderid, firstname, surname, companyname, nip, street, streetno, placeno, postcode, place, phone, email, encryption_key=None): 
    """
    Tworzenie nowych danych płatnika 

    :param int orderid: Id zamówienia
    :param str firstname: Imię
    :param str surname: Nazwisko
    :param str companyname: Nazwa firmy
    :param str nip: Numer NIP
    :param str street: Ulica
    :param str streetno: Nr budynku
    :param str placeno: Nr lokalu
    :param str postcode: Kod pocztowy
    :param str place: Miejscowość
    :param str phone: Telefon
    :param str email: Email
    :param str encryption_key: Hash szyfrowania bazy
    """

    cur = db.cursor()

    data = {}
    data['orderid'] = orderid
    data['firstname'] = firstname
    data['surname'] = surname
    data['companyname'] = companyname
    data['nip'] = nip
    data['street'] = street
    data['streetno'] = streetno
    data['placeno'] = placeno
    data['postcode'] = postcode
    data['place'] = place
    data['phone'] = phone
    data['email'] = email
    data['encryption_key'] = encryption_key
    

    sql = """
        INSERT INTO orderclientdata SET
            orderid = %(orderid)s, 
            firstname = AES_ENCRYPT(%(firstname)s, %(encryption_key)s), 
            surname = AES_ENCRYPT(%(surname)s, %(encryption_key)s),
            place = AES_ENCRYPT(%(place)s, %(encryption_key)s),
            companyname = AES_ENCRYPT(%(companyname)s, %(encryption_key)s),
            nip = AES_ENCRYPT(%(nip)s, %(encryption_key)s),
            postcode = AES_ENCRYPT(%(postcode)s, %(encryption_key)s),  
            phone = AES_ENCRYPT(%(phone)s, %(encryption_key)s),
            email = AES_ENCRYPT(%(email)s, %(encryption_key)s),
            street = AES_ENCRYPT(%(street)s, %(encryption_key)s), 
            streetno = AES_ENCRYPT(%(streetno)s, %(encryption_key)s),
            placeno = AES_ENCRYPT(%(placeno)s, %(encryption_key)s)
        """

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    orderclientid = cur.lastrowid
    return orderclientid

 
