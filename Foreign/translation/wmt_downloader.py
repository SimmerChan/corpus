# encoding=utf-8

"""
@author: SimmerChan

@email: hsl

@file: wmt_downloader.py

@desc:
"""

import requests
from tqdm import tqdm
import lxml.html as html
import os
import time


def download_file(name, url):
    def format_float(num):
        return '{:.2f}'.format(num)

    headers = {'Proxy-Connection': 'keep-alive'}
    r = requests.get(url, stream=True, headers=headers)
    length = float(r.headers['content-length'])
    f = open(name, 'wb')
    count = 0
    count_tmp = 0
    tqdm_data = tqdm(r.iter_content(chunk_size=512))
    tmp_time = time.time()
    for chunk in tqdm_data:
        if chunk:
            f.write(chunk)
            count += len(chunk)
            if time.time() - tmp_time > 4:
                p = count / length * 100
                speed = (count - count_tmp) / 1024 / 1024 / 4
                count_tmp = count
                state = name + ': ' + format_float(p) + '%' + ' Speed: ' + format_float(speed) + 'M/S'
                tqdm_data.set_description(state)
    f.close()


def download(root_link, prefix='news-commentary'):
    """
    下载news-commentary或者wikititle语料
    :param root_link: 下载网址根目录
    :param prefix: 文件名称前缀
    :return:
    """
    content = requests.get(root_link).content
    dom = html.document_fromstring(content)
    file_names = [name for name in dom.xpath('//td/a/@href') if name.startswith(prefix)]
    num = len(file_names)
    for index, file_name in enumerate(file_names):
        download_path = os.path.join(root_link, file_name)
        download_file(file_name, download_path)
        print('Download {}/{}'.format(index+1, num))


if __name__ == '__main__':
    download('http://data.statmt.org/news-commentary/v14/training/', 'news-commentary')
    download('http://data.statmt.org/wikititles/v1/', 'wikititles')