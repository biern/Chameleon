import os

for filename in os.listdir(os.path.dirname(__file__)):
    if filename.startswith("_") or not filename.endswith(".py"):
        continue

    # exec("import commands.{}".format(os.path.splitext(filename)[0]))
    __import__("{}".format(os.path.splitext(filename)[0]), globals(), locals())
