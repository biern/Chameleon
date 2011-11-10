# -*- coding: utf-8 -*-

from chameleon import api


@api.register
def add_product(db, title, stock, value=2):
    """
    Some docs

    :param str title: Nazwa produktu
    :param int stock: Liczba w magazynie
    :param float value: Cena
    """
    print("lol! dodałem produkt: {}; {}; {};".format(title, stock, value))
