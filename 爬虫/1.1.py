from urllib import request
from bs4 import BeautifulSoup
import re


html = request.urlopen("http://ssdut.dlut.edu.cn/index/bkstz.htm").read().decode('utf-8')
# print(html)
# res = re.findall(r'href="(.*?)"', html)
# print(res)

soup = BeautifulSoup(html, features='lxml')
# print(soup.h1)
# all_href = soup.find_all('a')
# all_href = [l["href"]for l in all_href]
# print('\n', all_href)

all_href = soup.find_all('a', {"class": "c56628"})
for link in all_href:
    print(link.get('href'))



