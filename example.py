# coding=utf-8
import requests

website1 = 'http://www.heibanke.com/accounts/login'
website2 = 'http://www.heibanke.com/lesson/crawler_ex02'
wrongNotify = '您输入的密码错误, 请重新输入'

s = requests.Session()
s.get(website1)     # 访问登录页面获取登录要用的csrftoken
token1 = s.cookies['csrftoken']      # 保存csrftoken
# 将csrftoekn存入字段csrfmiddlewaretoken
dataWebsite1 = {'username': 'user',
                'password': 'password',
                'csrfmiddlewaretoken': token1
                }
html = s.post(website1, data=dataWebsite1).content.decode('utf-8')
print(html)