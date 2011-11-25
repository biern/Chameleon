import logging
import os

log = logging.getLogger("Commands")

for filename in os.listdir(os.path.dirname(__file__)):
    if filename.startswith("_") or not filename.endswith(".py"):
        continue

    try:
        exec("from {0} import *".format(os.path.splitext(filename)[0]))
    except ImportError, e:
        log.error('Error while importing file "{0}": {1}'.format(
                filename, e))
    # __import__("{}".format(os.path.splitext(filename)[0]), globals(), locals())
