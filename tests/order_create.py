# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../src')

from chameleon.db import Database
from chameleon.commands import *

import time


if __name__ == "__main__":
    # Utworzenie nowego zamówienia
    orderId = order_create(db, 15, 5, "Opinia") 
    
    # Utworzenie informacji na temat płatnika
