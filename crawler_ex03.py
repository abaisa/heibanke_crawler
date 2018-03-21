import requests
import bs4

url_login = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex03/'

#模拟登陆
s = requests.Session()
s.get(url_login)
token1 = s.cookies['csrftoken']
data1 = {'username': 'abaisa','password': 'qwert6','csrfmiddlewaretoken': token1}
s.post(url_login, data=data1).content.decode('utf-8')

#获取密码
url_list = 'http://www.heibanke.com/lesson/crawler_ex03/pw_list/?page=1'
html = s.get(url_list).content.decode('utf-8')
print(html)