.. _`howitsmade`:

Jak to działa
=============

Dodawanie obrazków
------------------

Gdy dodajemy obraz do bazy danych / sklepu (np korzystając z ``image_add``) mają miejsce następujące wydarzenia:

#. Obraz jest odczytywany z lokalnej ścieżki w systemie plików
#. Program pobiera jego mimietype, a na tej podstawie pobiera jego filetypeid korzystając z tabeli filetype
#. Program identyfikuje id jego rozszerzenia na podstawie tabeli fileextensionid
#. Dodawany jest rekord do bazy danych identyfikujący plik, korzystając z wcześniej uzyskanych danych, uzyskujemy id zdjęcia
#. Obraz jest kopiowany do design/_gallery/_orginal/<id>.<ext>
#. Dla każdego z rozmiarów (50, 100, 200, 300) program generuje miniaturkę i umieszcza ją w katalogu design/_gallery/_<size>_<size>_<shopid>/<id>.<ext>

Pełna referencja i źródło (link po prawej stronie):

.. autoclass:: chameleon.commands.image_add.image_add

.. automethod:: chameleon.commands.image_add.perform
