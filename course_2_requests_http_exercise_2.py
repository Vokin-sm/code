import re
import requests

html = '<a href="http://stepic.org/courses"> ' \
       '<a href=\'https://stepic.org\'> ' \
       '<a href=\'http://neerc.ifmo.ru:1345\'> ' \
       '<a href="ftp://mail.ru/distib" > ' \
       '<a href="ya.ru"> ' \
       '<a href="www.ya.ru"> ' \
       '<a href="../skip_relative_links">'

url_list = re.findall(r'<a[^>]*?href=["\'](.*?)["\'][^>]*?>', html)
website_list = []

for el in url_list:
    website_list.extend(re.findall(r'([\w\-]+(?:\.[\w\-]+)+)', el))

website_list = set(website_list)
website_list = list(website_list)
website_list.sort()

[print(el) for el in website_list]


#for el in url_list:
    #website_list.extend(re.findall('.*//([^/:]*?)[/:].*', el))
#print(website_list)