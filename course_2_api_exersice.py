import requests

numbers = [960, 961, 997, 903, 938, 971, 919, 913, 912, 950, 951, 985, 924, 989, 927]
for number in numbers:
    api_url = "http://numbersapi.com/" + str(number) + "/math?json=true"
    res = requests.get(api_url)
    if res.json()["found"]:
        print("Interesting")
    else:
        print("Boring")


#print(res.status_code)
#print(res.headers["Content-Type"])
#print(res.json()["found"])
