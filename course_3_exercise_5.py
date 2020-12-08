s = "13 divide 3".split()

if s[1] == "plus":
    print(int(s[0]) + int(s[2]))
if s[1] == "minus":
    print(int(s[0]) - int(s[2]))
if s[1] == "multiply":
    print(int(s[0]) * int(s[2]))
if s[1] == "divide":
    print(int(s[0]) // int(s[2]))

