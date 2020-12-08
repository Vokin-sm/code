import requests
import re

url_2 = ["https://stepic.org/media/attachments/lesson/24472/sample2.html",
         "https://stepic.org/media/attachments/lesson/24472/sample0.html"]
url = []

for line in url_2:
    line = line.rstrip()
    url.append(line)


def get_url(link):
    res = requests.get(link)
    return re.findall(r"<a.*href=\"(.+)\">", res.text)


a = requests.get(url[0])
b = requests.get(url[1])

if a.status_code == 200 and b.status_code == 200:
    a_list = re.findall(r"<a.*href=\"(.+)\">", a.text)
    b_list = re.findall(r"<a.*href=\"(.+)\">", b.text)
    c_list = []

    if a_list:
        for u in a_list:
            if requests.get(u).status_code == 200:
                c_list.extend(get_url(u))

        if url[1] in a_list:
            if url[1] in b_list:
                print("Yes")
            else:
                if url[1] in c_list:
                    print("Yes")
                else:
                    print("No")
        else:
            if url[1] in c_list:
                print("Yes")
            else:
                print("No")
    else:
        print("No")
else:
    print("No")






