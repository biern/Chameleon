# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

from chameleon import Database
from chameleon.commands import add_product


if __name__ == "__main__":
    # Domyślne ustawienia bazy danych są zapisane w 'chameleon_conf.py',
    # można je też przeładować w konstruktorze:
    # Database(host='localhost', user='root', etc)
    db = Database()
    # test_call(db, 1, 2, 3, 4, 5, 6)
    add_product(db, title='Nowy produkt', stock=10, value=100)
