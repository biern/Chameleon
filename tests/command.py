# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

from chameleon import api, Database
from chameleon.commands import add_product


@api.register
def test_call(db, product_id, name, cost=1, etc='x', *args):
    """
    Robi coś bardzo ważnego i przydatnego

    :param int product_id: Id produktu
    :param int cost: Koszt
    """
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    print(cur.fetchone())


if __name__ == "__main__":
    # Domyślne ustawienia bazy danych są zapisane w 'chameleon_conf.py',
    # można je też przeładować w konstruktorze:
    # Database(host='localhost', user='root', etc)
    db = Database()
    db.connect()
    test_call(db, 1, 2, 3, 4, 5, 6)
    add_product(db, title='Nowy produkt', stock=10, value=100)
