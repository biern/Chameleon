# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

from chameleon import api, parse, Database


@api.register
def test_call(db, product_id, name, cost=1, etc='x', *args):
    """
    Robi coś bardzo ważnego i przydatnego

    :param int product_id: Id produktu
    :param int cost: Koszt
    """
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    print cur.fetchone()


if __name__ == "__main__":
    # parse()
    db = Database()
    db.connect()
    test_call(db, 1, 2, 3, 4, 5, 6)
