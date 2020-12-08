import json

student_1 = {
    "first name": "Greg",
    "last name": "Dean",
    "scores": [70, 80, 90],
    "description": "Good job, Greg",
    "certificate": True
}

student_2 = {
    "first name": "Wirt",
    "last name": "Wood",
    "scores": [80, 80.2, 80],
    "description": "Nicely done",
    "certificate": True
}

data = [student_1, student_2]
#print(json.dumps(data, indent=4, sort_keys=True))

#with open("student.json", "w") as f:
#    json.dump(data, f, indent=2, sort_keys=True)

#data_json = json.dumps(data, indent=4, sort_keys=True)
#data_again = json.loads(data_json)

#print(sum(data[0]["scores"]))
#print(sum(data_again[0]["scores"]))

with open("student.json", "r") as f:
    data_again = json.load(f)
    print(sum(data_again[1]["scores"]))