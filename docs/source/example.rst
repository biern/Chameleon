.. _`example`:

Przykład użycia
===============

Najpierw należy upewnić się, że polecenie ``chameleon`` odnalazło plik konfiguracyjny i nawiązuje połączenie z bazą danych. W tym celu wystarczy wywołać:

.. code-block:: bash

   $ chameleon

Jeśli aplikacja odnalazła plik konfiguracyjny i udało się nawiązać połączenie, powinny zostać wypisane możliwe polecenia.

Skrypt ``chameleon`` pozwala wywoływać wszystkie polecenia z API (:doc:`commands`) bezpośrednio z shella. Aby zobaczyć pełną dokumentację polecenia wystarczy dodać przełącznik ``-h``.


.. code-block:: bash

   $ chameleon product_add -h

   positional arguments:
     name                  Nazwa produktu
     url                   URL produktu
     stock                 Stan magazynowy
     vatid
     buyprice              Cena netto zakupu
     sellprice             Cena netto sprzedaży
     weight                Waga produktu

    optional arguments:
      -h, --help            show this help message and exit
      --languageid LANGUAGEID
                            Id języka (default: 1)
      --userid USERID       Id użytkownika (default: 1)

Argumenty pozycyjne (name, url, ...) są obowiązkowe, pozostałe można dodać lub nie stosując odpowiadjące im flagi.

.. code-block:: bash

   $ chameleon product_add "jakiś produkt" url 10 3 80 100 10 --userid 1

Warto zauważyć, że domyślne wartości dla tych argumentów są pobierane z pliku konfiguracyjnego (sekcja ``DEFAULT_ARGS``), jeśli chcemy, możemy je przeładować podając je explicite, jak powyżej.
