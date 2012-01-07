# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

from chameleon.db import Database
from chameleon.commands import *

if __name__ == "__main__":
    db = Database()

    # Utworzenie nowego zamówienia
    # Kurier standard
    # Płatność za pobraniem
    orderId = order_create(db, 25, 5, "Opinia klienta") 
    
    # Utworzenie nowych danych płatnika
    order_client(db, orderId, "Imię", "Nazwisko", "Nazwa firmy", "NIP", "Ulica" , "Nr budynku", "Nr lokalu", "11-111", "Miejscowość", "Telefon", "email@gekosaletest.pl")

    # Utworzenie nowych danych wysyłki
    order_delivery(db, orderId, "WImię", "WNazwisko", "WNazwa firmy", "WNIP", "WUlica", "WNr budynku", "WNr lokalu", "22-222", "WMiejscowość", "WTelefon", "email2@gekosaletest.pl") 

    # Dodanie nowego produktu do zakupów
    order_product(db, orderId, 21, 1, 6)

    # order_product(db, orderId, 22, 3)

    # Zmienienie statusu zamówienia
    order_status(db, orderId, 9, "Zmiana statusu")

    # Dodanie administratorskiej notatki na temat zamówienia
    order_note(db, orderId, "Treść notatki admina")
