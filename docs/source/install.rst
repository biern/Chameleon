.. _`install`:

Instalacja
==========

Projekt wymaga:

- `Python2.7`_ (wcześniejsze wersje nie zadziałają)
- python-mysqldb_
- PIL_

Instalacja zależności
---------------------

Python2.7
        Wersja 2.7 jest domyślna w większości zaktualizowanych systemów GNU/Linux. Aktualną wersję można sprawdzić poprzez ``python --version``. Jeśli doinstalowanie wersji 2.7 było konieczne, może zaistnieć konieczność wywoływania polecenia w wersji 2.7 explicite, stosując wszędzie ``python2.7`` zamiast ``python``.

python-mysqldb, PIL:
        Jeśli korzystamy z systemu GNU/Linux, jest duża szansa, że zależności te można pobrać instalując paczki ``python-mysqldb`` i ``python-imaging``. Jeśli nie, należy postępować zgodnie z instrukcjami na stronach bibliotek.


.. _PIL: http://www.pythonware.com/products/pil/
.. _python-mysqldb: http://sourceforge.net/projects/mysql-python/
.. _python2.7: http://www.python.org/getit/releases/2.7/


Instalacja programu
-------------------

.. code-block:: bash

   svn co http://xp-dev.com/svn/Sim2011_D.5-6 Chameleon

opcjonalne:
   instalacja jako globalnie dostępnego modułu pythona
   i utworzenie dowiązania w przestrzeni nazw użytkownika

.. code-block:: bash

   cd Chameleon
   sudo python setup.py install

Jeśli wykonaliśmy ostatni krok, w systemie powinno być dostępne polecenie ``chameleon``

Jeśli nie chcemy instalować paczki globalnie, można korzystać zamiennie ze skryptu ``tests/chameleon``

.. code-block:: bash

   cd Chameleon/tests
   ./chameleon

.. _conf-example:

Konfiguracja
------------

Projekt do działania wymaga utworzenia pliku konfiguracyjnego gdzieś w drzewie katalogów, w którym został uruchomiony. Skrypt przeszukuje katalogi w górę, poczynając od aktualnego, w poszukiwaniu pliku ``chameleon_conf.py``.

Przykładowy plik konfiguracyjny:

.. code-block:: python

   # -*- coding: utf-8 -*-

   # Konfiguracja bazy danych
   DATABASE = {
     'db': 'gekosale',
     'user': 'uzytkownik_bazy_danych',
     'passwd': 'haslo_bazy_danych',
     'host': 'ip/host_bazy_danych',
     'port': 3306,
     'connect_timeout': 3,
   }

   # Zestaw domyślnych argumentów dla wszystkich poleceń. Można go rozszerzyć
   # o własne, lub w ogóle pominąć jednak oszczędza on przesyłania za każdym
   # razem tych samych wartości do wszystkich wywołań.
   DEFAULT_ARGS = {
     # 'Pospilite' parametry:
     'userid': 1, # oznacza użytkownika, w którego imię skrypt przeprowadza akcje
     'languageid': 1, # id języka dla którego wprowadzamy tłumaczenia
     'shopid' : 3, # id sklepu w którym wprowadzamy zmiany

     # Parametry wykorzystywane tylko przez niektóre polecenia:

     # Absolutna ścieżka do miejsca instalacji gekosale,
     # czyli katalog w ktorym znajduje się 'index.php'.
     'root_path' : '/usr/local/zend/apache2/htdocs/gekosale',

     # Klucz szyfrujący z pliku $root_path/config/settings.php,
     # zapisany w 'client_data_encription_string'
     'encryption_key' : 'eaf3b0d871ca966048deb427f54d35d7',
   }

Jeśli korzystamy ze skryptu tests/chameleon , należy zastąpić istniejący plik tests/chameleon_conf.py własnymi ustawieniami.
