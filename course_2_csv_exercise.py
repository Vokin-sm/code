import csv
from collections import Counter

primary_type = []
type_max = 0

with open("Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if "2015" in row[2]:
            primary_type.append(row[5])

prim = Counter(primary_type)
print(prim)

#for el_set in set(primary_type):
#    i = 0
#    for el_list in primary_type:
#        if el_list == el_set:
#            i += 1
#    if i > type_max:
#        type_max = i
#        primary_type_max = el_set




