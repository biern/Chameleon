# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

from chameleon.db import Database
from chameleon.commands import *

import time


if __name__ == "__main__":
    uniqId = str(int(time.time()))
    db = Database()

    # Utworzenie nowej kategorii
    categoryId = category_add(db, "Nowa kategoria "+uniqId, "nowa_kategoria_url_"+uniqId, "Krótki opis",
                                          "Dłuższy opis", "Meta tytuł", "Słowa kluczowe",
                                          "Meta opis")

    # Utworzenie głównej kategorii
    mainCategoryId = category_add(db, "Nowa kategoria główna "+uniqId, "nowa_kategoria_glowna_url_"+uniqId, "Krótki opis główny",
                                          "Dłuższy opis główny", "Meta tytuł główny", "Słowa kluczowe główne",
                                          "Meta opis główne")

    # Ustawiamy główną kategorię
    category_change_main(db, categoryId, mainCategoryId)

    # Utworzenie nowego dostawcy
    delivererId = deliverer_add(db, "Nowy dostawca "+uniqId, "www.strona_dostawcy.pl", "email@dostawcy002.pl")

    # Utworzenie nowego producenta
    producerId = producer_add(db, "Nowy producent "+uniqId, "nowy_producent_url_"+uniqId, "opis nowego producenta")

    # Utworzenie nowego produktu i dodanie go do nowo utworzonej
    # kategori, dostawcy i producenta
    # 1 - stan magazynowy
    # 5 - VAT-ID
    # 100.10 - Cena zakupu
    # 200.30 - Cena sprzedaży
    # 10.50 - Waga
    productId = product_add(db, "Nowy dodany produkt "+uniqId, "url_dodanego_produktu_"+uniqId, 1, 5, 100.10, 200.30, 10.50)

    # Ustawiamy kategorię dla tego produktu
    product_add_to_category(db, productId, categoryId)
    product_add_to_category(db, productId, mainCategoryId)

    # Uzupełnienie podstawowych informacji w produkcie
    product_edit_basic_information(db, productId, 1, "KOD EAN", "Kod dostawcy", producerId, delivererId)

    # Uzupełnienie meta informacji
    product_edit_meta(db, productId, "Meta tytuł", "Słowa kluczowe", "Meta opis")

    # Uzupełnianie opisu
    product_edit_description(db, productId, "Krótki opis", "Normalny opis", "Dodatkowe informacje")

    # Ustawienie informacji o dostawie i magazynie
    product_edit_stock(db, productId, 100, 1, 100.45)

    # Dodanie zdjęcia do gekosale
    imageId = image_add(db, sys.argv[1])

    # Dodanie zdjęcia do produktu i ustawienie go jako główne
    product_add_image(db, productId, imageId)

    # Tworzymy nową grupę cech
    attributeGroupId = attribute_add_group(db, "Nowa grupa cech "+uniqId)

    # Dodajemy nowe cechy
    attributePropertyId = attribute_add_property(db, attributeGroupId, "Wielkość "+uniqId)

    # Dodajemy cechę do utworzonej kategorii
    attribute_add_to_category(db, attributeGroupId, attributePropertyId, categoryId)

    # Dodajemy wartości do cechy
    xValueId = attribute_add_value(db, "Wielkość X "+uniqId, attributePropertyId);

    lValueId = attribute_add_value(db, "Wielkość L "+uniqId, attributePropertyId);

    # Dodajemy nowy wariant produktu i ustalamy jego właściwości
    # 2 - typ (w tym wypadku dodawanie)
    variantId = product_add_variant(db, productId, 2, 456.10, 20, attributeGroupId, "symbol", 177)

    # Do danego wariantu przypisujemy cechę Wielkość L
    variant_add_value(db, variantId, lValueId)

    print("OK")


