import re

line = "this is a text \"this' !is. ?n1ce,"

line = re.sub(r"\b(\w)(\w)", r"\2\1", line)
print(line)
