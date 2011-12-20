# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

from chameleon.commands import *

import time
from chameleon.db import Database

if __name__ == "__main__":
    uniqId = str(int(time.time()))

    # Utworzenie nowej kategorii
    categoryId = category_add(Database(), "Nowa kategoria "+uniqId, "nowa_kategoria_url", "Krótki opis",
                                          "Dłuższy opis", "Meta tytuł", "Słowa kluczowe",
                                          "Meta opis")

    # Utworzenie głównej kategorii
    mainCategoryId = category_add(Database(), "Nowa kategoria główna "+uniqId, "nowa_kategoria_glowna_url", "Krótki opis główny",
                                          "Dłuższy opis główny", "Meta tytuł główny", "Słowa kluczowe główne",
                                          "Meta opis główne")

    # Ustawiamy główną kategorię
    category_change_main(Database(), categoryId, mainCategoryId)

    # Utworzenie nowego dostawcy
    delivererId = deliverer_add(Database(), "Nowy dostawca "+uniqId, "www.strona_dostawcy.pl", "email@dostawcy002.pl")

    # Utworzenie nowego producenta
    producerId = producer_add(Database(), "Nowy producent "+uniqId, "nowy_producent_url", "opis nowego producenta")

    # Utworzenie nowego produktu i dodanie go do nowo utworzonej
    # kategori, dostawcy i producenta
    # 1 - stan magazynowy
    # 5 - VAT-ID
    # 100.10 - Cena zakupu
    # 200.30 - Cena sprzedaży
    # 10.50 - Waga
    productId = product_add(Database(), "Nowy dodany produkt "+uniqId, "url_dodanego_produktu", 1, 5, 100.10, 200.30, 10.50)

    # Ustawiamy kategorię dla tego produktu
    product_add_to_category(Database(), productId, categoryId)
    product_add_to_category(Database(), productId, mainCategoryId)

    # Uzupełnienie podstawowych informacji w produkcie
    product_edit_basic_information(Database(), productId, 1, "KOD EAN", "Kod dostawcy", producerId, delivererId)

    # Uzupełnienie meta informacji
    product_edit_meta(Database(), productId, "Meta tytuł", "Słowa kluczowe", "Meta opis")

    # Uzupełnianie opisu
    product_edit_description(Database(), productId, "Krótki opis", "Normalny opis", "Dodatkowe informacje")

    # Ustawienie informacji o dostawie i magazynie
    product_edit_stock(Database(), productId, 100, 1, 100.45)

    # Dodanie zdjęcia do gekosale
    imageId = image_add(Database(), sys.argv[1])

    # Dodanie zdjęcia do produktu i ustawienie go jako główne
    product_add_image(Database(), productId, imageId)

    # Tworzymy nową grupę cech
    attributeGroupId = attribute_add_group(Database(), "Nowa grupa cech "+uniqId)

    # Dodajemy nowe cechy
    attributePropertyId = attribute_add_property(Database(), attributeGroupId, "Wielkość "+uniqId)

    # Dodajemy cechę do utworzonej kategorii
    attribute_add_to_category(Database(), attributeGroupId, attributePropertyId, categoryId)

    # Dodajemy wartości do cechy
    xValueId = attribute_add_value(Database(), "Wielkość X "+uniqId, attributePropertyId);

    lValueId = attribute_add_value(Database(), "Wielkość L "+uniqId, attributePropertyId);

    # Dodajemy nowy wariant produktu i ustalamy jego właściwości
    # 2 - typ (w tym wypadku dodawanie)
    variantId = product_add_variant(Database(), productId, 2, 456.10, 20, attributeGroupId, "symbol", 177)

    # Do danego wariantu przypisujemy cechę Wielkość L
    variant_add_value(Database(), variantId, lValueId)

    print "OK"


