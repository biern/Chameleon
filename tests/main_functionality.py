# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '../src')
from chameleon.commands import *

from chameleon.db import Database

if __name__ == "__main__":
    # Utworzenie nowej kategorii
    categoryId = category_add(Database(), "Nowa kategoria", "nowa_kategoria_url", "Krótki opis",
                                          "Dłuższy opis", "Meta tytuł", "Słowa kluczowe",
                                          "Meta opis")
    print categoryId
    
    
