import threading
import requests
from bs4 import BeautifulSoup

count = 0
res_list = [-1] * 101

# 模拟登陆
def login():
    url_login = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex03/'
    s = requests.Session()
    s.get(url_login)
    token1 = s.cookies['csrftoken']
    data1 = {'username': 'abaisa', 'password': 'qwert6', 'csrfmiddlewaretoken': token1}
    s.post(url_login, data=data1)
    return s

def getHtml(threadName, s):
    global count
    while count < 100:
        # 获取网页
        url_list = 'http://www.heibanke.com/lesson/crawler_ex03/pw_list/?page=1'
        html = s.get(url_list).content.decode('utf-8')
        # 读取密码数字
        global res_list
        soup = BeautifulSoup(html, "lxml")
        page_res_set = soup.find_all('td')
        i = 2
        while i < 18:
            pos = int(page_res_set[i].string)
            key = int(page_res_set[i + 1].string)
            if res_list[pos] == -1:
                count += 1
            if res_list[pos] != -1 and res_list[pos] != key:
                print("ERROR !!!!")
            res_list[pos] = key
            i += 2
            print(threadName + ': ' + str(pos) + '--' + str(key) + '  count:' + str(count))


s = login()
# 创建2个线程 这里又问题，超过两个不知道为什么会有错误
for i in range(2):
    threading.Thread(target=getHtml, args = (('T-' + str(i)), s)).start()


# 这段代码是再ipython中执行的没有验证。太慢了，放在这了
res = list(map(lambda x:str(x), res_list))
res_str = "".join(res)

print(res_str)

# 答案 5382536752649723381830867445135357748950695244329548946136479903948743260484371348776618136963449163