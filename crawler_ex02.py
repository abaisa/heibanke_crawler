# coding=utf-8
import requests

url1 = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'
url2 = 'http://www.heibanke.com/lesson/crawler_ex02/'
wrongNotify = '您输入的密码错误, 请重新输入'

#模拟登陆
s = requests.Session()
s.get(url1)
token1 = s.cookies['csrftoken']
data1 = {'username': 'abaisa','password': 'qwert6','csrfmiddlewaretoken': token1}
html1 = s.post(url1, data=data1).content.decode('utf-8')

print('-----------')

i = 1
while i < 30:
    i = i + 1
    s.post(url2)
    token2 = s.cookies['csrftoken']
    data2 = {'csrfmiddlewaretoken' : token2, 'username' : 'abaisa', 'password': i}
    html2 = s.post(url2, data=data2).content.decode('utf-8')
    if wrongNotify not in html2:
        print(i)
        break