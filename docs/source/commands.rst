.. _`commands`:

Pełna referencja API
====================

Dostępne wywołania API
----------------------

Przy wywoływaniu metod z linii poleceń pierwszy argument, ``db`` czyli
bazę danych należy pominąć. Zostaje ona stworzona i przesłana
automatycznie na podstawie pliku konfiguracyjnego znajdującego się w
drzewie katalogów. (tutaj link)

.. Generacja tej listy:
   ls ../src/chameleon/commands/*.py | cut -d "/" -f 5 | cut -d "." -f 1 | sort | grep -v __init__ | xclip -i

attribute_add_group
^^^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.attribute_add_group.perform

attribute_add_property
^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.attribute_add_property.perform

attribute_add_to_category
^^^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.attribute_add_to_category.perform

attribute_add_value
^^^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.attribute_add_value.perform

category_add
^^^^^^^^^^^^

.. automethod:: chameleon.commands.category_add.perform

category_change_main
^^^^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.category_change_main.perform

deliverer_add
^^^^^^^^^^^^^

.. automethod:: chameleon.commands.deliverer_add.perform

image_add
^^^^^^^^^

.. automethod:: chameleon.commands.image_add.perform

order_client
^^^^^^^^^^^^

.. automethod:: chameleon.commands.order_client.perform

order_create
^^^^^^^^^^^^

.. automethod:: chameleon.commands.order_create.perform

order_delivery
^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.order_delivery.perform

order_note
^^^^^^^^^^

.. automethod:: chameleon.commands.order_note.perform

order_product
^^^^^^^^^^^^^

.. automethod:: chameleon.commands.order_product.perform

order_status
^^^^^^^^^^^^

.. automethod:: chameleon.commands.order_status.perform

producer_add
^^^^^^^^^^^^

.. automethod:: chameleon.commands.producer_add.perform

producer_add_deliverer
^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.producer_add_deliverer.perform

product_add
^^^^^^^^^^^

.. automethod:: chameleon.commands.product_add.perform

product_add_image
^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.product_add_image.perform

product_add_to_category
^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.product_add_to_category.perform

product_add_variant
^^^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.product_add_variant.perform

product_edit_basic_information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.product_edit_basic_information.perform

product_edit_description
^^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.product_edit_description.perform

product_edit_meta
^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.product_edit_meta.perform

product_edit_stock
^^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.product_edit_stock.perform

products_csv_import
^^^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.products_csv_import.perform

.. products_dir_update
.. ^^^^^^^^^^^^^^^^^^^

.. .. automethod:: chameleon.commands.products_dir_update.perform

product_update
^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.product_update.perform

variant_add_value
^^^^^^^^^^^^^^^^^

.. automethod:: chameleon.commands.variant_add_value.perform
