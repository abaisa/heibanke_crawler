import requests

url = 'http://www.heibanke.com/lesson/crawler_ex01/'
i = 0
wrongNotify = '您输入的密码错误, 请重新输入'
data = {'csrfmiddlewaretoken' : 'rZGs8NfjfKoqO7aId4nPYya7kO3Cg0Bl', 'username' : 'abaisa', 'password': i}
html = requests.post(url, data).content.decode('utf-8')
while wrongNotify in html:
    data = {'csrfmiddlewaretoken' : 'rZGs8NfjfKoqO7aId4nPYya7kO3Cg0Bl', 'username' : 'abaisa', 'password': i}
    print(i)
    i = i + 1
    html = requests.post(url, data).content.decode('utf-8')
