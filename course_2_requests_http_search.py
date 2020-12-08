import requests

res = requests.get("https://yandex.ru/search/", params={"text": "stepic",
                                                        "test": "test1",
                                                        "name": "Name with spaces",
                                                        "list": ["test1", "test2"]
                                                        })

print(res.status_code)
print(res.headers["Content-Type"])
print(res.url)
#print(res.text)