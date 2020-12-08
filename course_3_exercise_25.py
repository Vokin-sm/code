units = {
    "mile": 1609,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254,
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    "mm": 0.001
}

s = "15.5 m in km".split()

number = (units[s[1]] * float(s[0])) / units[s[3]]
print(number)#("{:.2e}".format(number))