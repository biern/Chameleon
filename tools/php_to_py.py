""" Very simple syntax and specific logic conversion tool from php->py """

import re
import sys


data_execute = \
"""
cur = db.cursor()
cur.execute(sql, data)
db.commit()
"""


if __name__ == "__main__":
    for line in open(sys.argv[1]):
        # spaces
        m = re.search("^( *)(.*)", line)
        spaces = m.group(1)
        line = m.group(2)

        # syntax
        line = line.replace("$", "")
        line = line.replace("->", ".")
        line = re.sub(r":(\w+)", r"%(\1)s", line)
        line = re.sub(r";\s*$", "\n", line)
        line = re.sub(r"if\s\((.*)\)(.*)", r"if \1:", line)
        line = re.sub(r"public\s+function(.*)", r"@api.register\ndef\1:", line)
        line = re.sub(r"[\{|\}]", "", line)
        line = re.sub(r"array\s*\(", "{", line)
        line = re.sub(r"(=>[^\)]*)\)", r"\1}", line)
        line = re.sub(r"\s*=>\s*", ": ", line)
        line = re.sub(r"^(\s*)/\*\*", r'"""', line)
        line = re.sub(r"^(\s*)\*/", r'"""', line)
        line = re.sub(r"^(\s*)\*", r'', line)

        # docstrings
        line = re.sub(r"@param +(\S+) +(\S+) (.*)",
                      r":param \1 \2: \3", line)

        # logic
        line = line.replace("stmt", "data")
        line = re.sub(r"(\w+) * = *data.executeInsertId\(\)",
                      r"data.execute()\n\1 = cur.lastrowid", line)
        line = re.sub(r"data.execute(\w+)\((.*)",
                      r"data.execute(\2",  # "#was: execute\1",
                      line)
        line = re.sub(r"this\.db\.prepare.*", r" {}", line)
        line = line.replace("this.check", "db.validate")
        line = re.sub(r'data\.set(\w+)\((.*), *(.*)\)',
                      r'data[\2] = \3', line)
        line = line.replace("data.execute()", data_execute)

        # fixing spaces and newlines
        if not line or line[-1] != "\n":
            line += "\n"

        line = re.sub(r"\n([^\n]+)", "\n" + spaces + r"\1", line,
                      flags=re.MULTILINE)

        sys.stdout.write(spaces + line)
