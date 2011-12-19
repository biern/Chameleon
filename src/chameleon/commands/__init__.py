import logging
import os

log = logging.getLogger("Commands")

__all__ = []

for filename in os.listdir(os.path.dirname(__file__)):
    if filename.startswith("_") or not filename.endswith(".py"):
        continue

    mod_name = os.path.splitext(filename)[0]

    try:
        exec("from {0} import *".format(mod_name))
        __all__.append(mod_name)
    except ImportError, e:
        log.error('Error while importing file "{0}": {1}'.format(
                filename, e))
    # __import__("{}".format(os.path.splitext(filename)[0]), globals(), locals())
