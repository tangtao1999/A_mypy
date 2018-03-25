from bs4 import BeautifulSoup
import re
import random
from urllib import request
# base_url = "http://global.bing.com"
base_url = "http://baike.baidu.com"
his = ["/item/Hermione/2283394?fr=aladdin"]
ans_url = []
for i in range(20):
    url = base_url + his[-1]
    html = request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    sub_url = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/[赫敏]hermione(%.{2})+$")})
    temp = soup.find_all("div", {"class": "para"}).get_text()
    ans = re.finditer("我觉得人们都在等我搞砸了", temp)
    if len(ans) != 0:
        ans_url.append(url)
        print(soup.find('h1').get_text(), 'url', url)
    if len(sub_url) != 0:
        his.append(random.sample(sub_url, 1)[0]["href"])
    else:
        his.pop()
