import requests
import re
import time
import random
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
}
for page in range(1, 11):
    print(f'正在爬取第{page}页数据')
    baseurl = f"https://wallpaperscraft.com/catalog/anime/page{page}"
    #response是第一级页面的源码
    #response = requests.get(baseurl, headers=headers)
    response = requests.get(baseurl, headers=headers)
    # response.keep_alive = False
            # 处理正常响应的逻辑
    # print("第一次请求成功")
    results = re.findall('class="wallpapers__link" href="/wallpaper(.*?)"', response.text)
    max_chapter_count = 10
    for result in results[:max_chapter_count]:
        picurl =('https://images.wallpaperscraft.com/image/single/' + result + '_1920x1080.jpg')
        print(picurl)
        # https: // images.wallpaperscraft.com / image / single / puppy_husky_down_53643_1920x1080.jpg
        # https: // images.wallpaperscraft.com / image / single / black_cat_muzzle_look_117261_1920x1080.jpg
        # for x in picurl:
        #     reyx = requests.get(url=picurl, headers=headers)
        # #     # 处理正常响应的逻辑
        # #     # print(reyx)
        #     y = re.findall('<a class="JS-Popup" href="(.*?)">', reyx.text)[max_chapter_count]
        #     print(y)
        #     delay = random.uniform(1, 5)
        #     time.sleep(delay)
        picurl_data = requests.get(url=picurl, headers=headers).content
        # print("第三次请求成功")
        # print(picurl_data)
        with open('pic3\\' + result + '.jpg', mode='wb') as f:
            f.write(picurl_data)
            print('保存完成')