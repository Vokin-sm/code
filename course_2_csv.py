import csv

#with open("example.csv") as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print(row)


#with open("example.tsv") as h:
#    reader = csv.reader(h, delimiter="\t")
#    for row in reader:
#        print(row)

students = [
    ["Greg", "Dean", 70, 80, 90, "Good jod, Greg"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]

with open("example_2.csv", "a") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(students)