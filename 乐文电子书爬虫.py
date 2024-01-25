import requests
import re
import time
from bs4 import BeautifulSoup
mainURL = 'https://www.lewen01.com/book/113761/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50',
}
#print(mainText)
#<dd><a href="(.*?)" title=".*?">(.*?)</a></dd>
#print(info_list)
for i in range(1, 730):
    url = mainURL + str(i) +'.html'
    #print(url)
    response = requests.get(url, headers=headers)
    html_data = response.text
#print(response.text)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    content = soup.find(attrs={'id': 'chaptercontent'}).text
    content = re.sub(r'\s+', '\n\n', content)
    content = re.sub(r'『点此报错』『加入书签』', '', content)
    content = re.sub(r'请收藏本站：https://www.lewen01.com。乐文小说网手机版：https://m.lewen01.com', '(本章完)', content)
    title = soup.find('h1').text
    x = title + '\n' + content + '\n\n'
    print(content)
    f = open('国王.txt',mode='a',encoding='utf-8')
    f.write(x)
#print('爬取成功')