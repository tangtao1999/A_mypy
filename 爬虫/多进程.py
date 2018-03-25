import multiprocessing as mp
import time
from urllib.request import urlopen,urljoin
from bs4 import BeautifulSoup
import re

base_url = "https://morvanzhou.github.io"
def crawl(url):
    response = urlopen(url)
    time.sleep(0.1)
    return response.read().decode()
def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all('a', {
        "href": re.compile('^/.+?/$')
    })
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url["href"]) for url in urls])
    url = soup.find('meta', {
        'property': 'og:url'
    })['content']
    return title, page_urls, url
unseen = set([base_url,])
seen = set()
pool = mp.Pool()
count, t = 1, time.time()
while len(unseen) != 0:
    if len(seen) > 20:
        break
    crawl_jods = [pool.apply_async(crawl, args=(url,)) for url in unseen]
    htmls = [j.get() for j in crawl_jods]

    parse_jobs = [pool.apply_async(parse,args=(html,)) for html in htmls]
    results = [j.get() for j in parse_jobs]

    seen.update(unseen)
    unseen.clear()

    for title, page_urls, url in results:
        print(count, title, url)
        count += 1
        unseen.update(page_urls-seen)
print('total time:%.1f' % (time.time()-t,))
