from subprocess import run
import codecs
import urllib.request
from bs4 import BeautifulSoup
request = urllib.request.Request("http://ssdut.dlut.edu.cn/index/bkstz.htm")
text = urllib.request.urlopen(request).read()
soup = BeautifulSoup(text, "html.parser")
infos = soup.find_all("a", class_='c56628')
dates = soup.find_all("span", class_='c56628_date fr')
url = "http://ssdut.dlut.edu.cn/"
location = "学生周知.html"
fin = codecs.open(location, "w", "utf-8")
fin.write("<html>"+"\n")
fin.write("<head>"+"\n")
fin.write("<meta charset='utf-8' >")
fin.write("</head>"+"\n")
fin.write("<body>"+"\n")
fin.write("<div style=\"margin:0 auto;font-size:30px;text-align:center;margin-top:20px;\">"
          "学生周知<br/><span style=\"font-size:10px;font-family:\"Arial\"\">administrator:"
          "<span style=\"color:red;\">软1702tangtao</span></span></div>")
fin.write("<div id="+"\"news\""+"style=\"width:70%;margin:0 auto;\""+">"+"\n")
i = 0
for info in infos:
    fin.write("<a "+"style=\"float:left;clear:both;font-size:19px;line-height:1.5em;\""+
              "href="+urllib.request.urljoin("http://ssdut.dlut.edu.cn/", info.get("href"))+
              " target=\"_blank\""+">"+info.get("title")+"</a>"+"\n")
    fin.write("<span style=\"float:right;font-size:19px;line-height:1.5em;\">"+dates[i].get_text()+"</span>")
    i += 1
fin.write("</div>"+"\n")
fin.write("</body>"+"\n")
fin.write("</html>"+"\n")
fin.close()
run('学生周知.html', shell=True)
run('exit()', shell=True)
# os.system('学生周知.html')
# os.system('exit()')
# pyinstaller -F -w -i manage.ico app.py
# -F：打包为单文件
# -w：Windows程序，不显示命令行窗口
# -i：是程序图标，app.py是你要打包的py文件