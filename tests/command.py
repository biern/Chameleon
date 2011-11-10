# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

from chameleon import api


@api.register
def test_call(self, product_id, name, cost=1, etc='x', *args):
    """
    Robi coś bardzo ważnego i przydatnego

    :param int product_id: Id produktu
    :param int cost: Koszt
    """
    print(product_id, name, cost, etc, args)


if __name__ == "__main__":
    cmd = test_call.shell_eval(sys.argv[1:])
