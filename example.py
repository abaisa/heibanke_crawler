import requests
from bs4 import BeautifulSoup
import pickle

# 不知道密码位置是重0还是1开始
res_array = [-1] * 101
count = 0

f = open(r'exampleHtml.txt', mode='rb')
html = pickle.load(f)
f.close()

soup = BeautifulSoup(html, "lxml")

page_res_set = soup.find_all('td')
i = 2
while i < 18:
    pos = int(page_res_set[i].string)
    key = int(page_res_set[i + 1].string)
    if res_array[pos] == -1:
       count += 1
    if res_array[pos] != -1 and res_array[pos] != key:
        print("ERROR !!!!")
    res_array[pos] = key
    i += 2
