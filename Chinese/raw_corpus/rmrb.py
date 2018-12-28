# encoding=utf-8

"""

@author: SimmerChan

@github: https://github.com/SimmerChan

@zhihu: https://www.zhihu.com/people/simmerchan/

@wechat: 尘世美的小茶馆

@file: rmrb.py

@time: 2018/12/26 21:59

@desc: 把mysql存的新闻保存为文本文件

"""

import pymysql
import re


def news_dump(partial=True, start_time="1997-01-01 00:00:00", end_time="1999-01-01 00:00:00"):
    """
    取出指定时间段内的所有新闻。
    Args:
        partial: 取出部分新闻还是全部新闻
        start_time:新闻起始时间
        end_time: 新闻终止时间

    Returns:

    """

    # TODO 连接本地mysql的CBDB数据库
    mysql_db = pymysql.connect(host="localhost", user="root", db="rmrb", use_unicode=True, charset="utf8mb4")
    mysql_cursor = mysql_db.cursor()

    if not partial:
        mysql_cursor.execute('SELECT subject, content FROM rmrb.pw_threads, rmrb.pw_tmsgs where '
                             'rmrb.pw_threads.tid = rmrb.pw_tmsgs.tid')
    else:
        # TODO 数据库里面的时间是用Unix时间戳函数转换后再保存的，这里也转换一下。
        mysql_cursor.execute(
            'Select subject, content from rmrb.pw_threads, rmrb.pw_tmsgs where postdate > UNIX_TIMESTAMP("{0}") and postdate < UNIX_TIMESTAMP("{1}") and rmrb.pw_threads.tid = rmrb.pw_tmsgs.tid'.format(
                start_time, end_time))

    total_news = 0
    total_char = 0
    blank = re.compile(r'\s+')
    with open('./news.txt', 'w') as f:
        for r in mysql_cursor.fetchall():
            total_news += 1
            title = re.sub(blank, '', r[0].strip())
            content = re.sub(blank, '', r[1].strip())
            length = len(title + content)
            if length == 0:
                continue
            else:
                f.write(title + '\n' + content + '\n')
                total_char += length

    print(total_news)
    print(total_char)


news_dump()