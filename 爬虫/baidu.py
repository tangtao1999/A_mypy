from bs4 import BeautifulSoup
import re
import random
from urllib import request
base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fr=aladdin"]
for i in range(20):
    url = base_url + his[-1]
    html = request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(soup.find('h1').get_text(), 'url', base_url+his[-1])
    sub_url = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})
    if len(sub_url) != 0:
        his.append(random.sample(sub_url, 1)[0]["href"])
    else:
        his.pop()
