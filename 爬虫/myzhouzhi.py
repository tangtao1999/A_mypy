from bs4 import BeautifulSoup
from urllib import request
import codecs
from subprocess import run
html = request.urlopen('http://ssdut.dlut.edu.cn/index/bkstz.htm').read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
all_href = soup.find_all('a', class_='c56628')
all_date = soup.find_all('span', class_='c56628_date fr')
base_url = "http://ssdut.dlut.edu.cn/"
location = "学生周知.html"
f_html = codecs.open(location, "w", "utf-8")
f_html.write("<!DOCTYPE html>")
f_html.write("<html lang='en'>")
f_html.write("<head><meta charset=\"UTF-8\"><title>MyZhouZhi</title>")
f_html.write("<style type=\"text/css\">a:hover{color: red!important;font-size: 25px!important;}</style>")
f_html.write("<body><div style=\"margin:20px auto; text-align:center;\"><h1>学&nbsp生&nbsp周&nbsp知</h1>")
f_html.write("<p style=\"color:green\">By TangTao</p></div>")

i = 0
for href in all_href:
    f_html.write("<div class = \"news\" style=\"width:80%;margin:0 auto;\">")
    f_html.write("<a " + "style=\"font-size:19px;line-height: 1.5em;color:purple;text-decoration: none;\"" +
                 "href=" + request.urljoin(base_url, href.get('href')) + " target=\"_blank\"" + ">" + href.get("title")
                 + "</a>")
    f_html.write("<span style=\"float: right;font-size: 19px;line-height: 1.5em\">" +
                 all_date[i].get_text() + "</span></div>")
    i += 1
f_html.write("</body></html>")
f_html.close()
run('学生周知.html', shell=True)
run('exit', shell=True)

# C:\Users\15755\anaconda\envs\untitled> pyinstaller -F -w  D:\爬虫\myzhouzhi.py
# -F：打包为单文件
# -w：Windows程序，不显示命令行窗口

# 注意  1.每个便签之间的空格  2.引号要转义  3.优先级内联大于外联




