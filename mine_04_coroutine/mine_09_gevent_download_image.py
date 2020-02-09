import urllib.request
import gevent
import random
import string
from gevent import monkey

monkey.patch_all()


def downloader(image_url):
    req = urllib.request.urlopen(image_url)
    image_content = req.read()
    # 从a-zA-Z0-9生成指定数量的随机字符：
    image_name = ''.join(random.sample(string.ascii_letters + string.digits, 12))
    print(image_name)
    with open(image_name + ".jpg", "wb") as f:
        f.write(image_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "https://image3.suning.cn/uimg/nmps/MBLSPZT/10044338411541020177picH_1_200x200.jpg"),
        gevent.spawn(downloader, "https://image4.suning.cn/uimg/nmps/MBLSPZT/10044352910897563031picH_1_200x200.jpg")
    ])


if __name__ == '__main__':
    main()
