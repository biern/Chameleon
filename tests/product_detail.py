# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

from chameleon.db import Database
from chameleon.commands import *

if __name__ == "__main__":
    db = Database()

    # Ustawienie ceny promocyjnej dla produktu
    product_promotion(db, 10, 5, "2012-1-1", "2012-1-14")

    # Ustawienie produktu jako nowy
    product_set_new(db, 10, "2012-1-20"); 

    # Ustawiamy produkty podobne
    product_similar(db, 10, 11);

    # Ustawiamy sprzedaż krzyżową
    product_crosssell(db, 10, 11);
