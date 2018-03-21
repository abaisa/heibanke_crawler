import requests
import re

url = 'http://www.heibanke.com/lesson/crawler_ex00/'
page_content = requests.get(url)
print(page_content.content)
number = re.findall(r'输入数字([0-9]{5})',page_content.content.decode('utf-8'))
while number:
    url = 'http://www.heibanke.com/lesson/crawler_ex00/' + number[0]
    print(url)
    page_content = requests.get(url)
    number = re.findall(r'数字是([0-9]{5})', page_content.content.decode('utf-8'))
