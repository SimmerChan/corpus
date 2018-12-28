# encoding=utf-8

"""

@author: SimmerChan

@github: https://github.com/SimmerChan

@zhihu: https://www.zhihu.com/people/simmerchan/

@wechat: 尘世美的小茶馆

@file: cbdb.py.py

@time: 2018/12/28 15:00

@desc: 将CBDB中的数据转为简体字后存入Mysql数据库中

简繁转换脚本traditional2simple是网上找的，具体作者不详。

"""

import sqlite3
import pymysql
from Chinese.structural_data.tradition2simple.traditional2simple import tradition2simple
import re
import traceback
from collections import OrderedDict, defaultdict
import pyodbc


def dict_factory(cursor, row):
    """
    把sqlite中的记录转为字典
    :param cursor:
    :param row:
    :return:
    """
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# TODO 正则表达式过滤
chinese_pattern = re.compile(u'[\u4E00-\u9FA5]+')
question_mark_pattern = re.compile(u'\?')
illegal_pattern = re.compile(u'[^\u0000-\u9FA5]+')
space_pattern = re.compile(u' ')

# TODO 连接本地mysql的CBDB数据库
mysql_db = pymysql.connect(host="localhost", user="root", db="CBDB", use_unicode=True, charset="utf8mb4")

# TODO 用sqlite3读取CBDB数据库
sqlite_db_path = 'xxx'
sqlite_db = sqlite3.connect(sqlite_db_path)
row_factory = sqlite_db.row_factory

# TODO 用pyodbc链接CBDB的access数据库
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=E:\SimmerChan\lab\mywork\resources\20170829CBDBavBase\20170829CBDBavBase.mdb;'
    )
cnxn = pyodbc.connect(conn_str)

crsr = cnxn.cursor()
mysql_cursor = mysql_db.cursor()
sqlite_cursor = sqlite_db.cursor()

# TODO 获取mysql保留关键词
mysql_cursor.execute('SELECT * FROM mysql.help_keyword')
reserved_keywords = [i[1] for i in mysql_cursor.fetchall()]

# TODO 获取所有表名
name_of_all_tables = [i[0] for i in sqlite_cursor.execute("select name from sqlite_master where type = 'table' order by name").fetchall()]

# TODO 获取所有表的主键和不含主键的表名
pk_of_table = defaultdict(list)
for table_name in name_of_all_tables:
    for row in crsr.statistics(table_name, unique=True):
        if row[5] is not None:
            if row[5].replace(' ', '').lower().find('primarykey') != -1:
                pk_of_table[table_name].append(row[8])

    if len(pk_of_table[table_name]) == 0:
        for row in crsr.statistics(table_name, unique=True):
            pk_of_table[table_name].append(row[8])

for k, v in sorted(pk_of_table.items(), key=lambda item: item[0]):
    if v[0] is not None:
        pk_str = 'primary key ('
        for pk in v:
            pk_str += pk + ','
        pk_str = pk_str[:-1] + ')'
        pk_of_table[k] = pk_str
    else:
        del pk_of_table[k]

# TODO 记录有duplicate key的表
# table_with_dk = defaultdict(tuple)

name_of_table_with_PK = pk_of_table.keys()

print('Total tables which contains PK: {0}'.format(len(name_of_table_with_PK)))
for index, table_name in enumerate(name_of_table_with_PK):
    print('{0}.Table {1} transferring...................'.format(index + 1, table_name))
    # TODO 还原sqlite的row factory
    sqlite_db.row_factory = row_factory
    sqlite_cursor = sqlite_db.cursor()

    # TODO 获取此表每个字段的类型
    field_types = OrderedDict()
    field_with_type = ''
    fields_str = ''
    values_str = ''
    for i in sqlite_cursor.execute("PRAGMA TABLE_INFO({0})".format(table_name)).fetchall():
        # TODO 给带空格的字段加下划线
        field_name = i[1]

        if field_name.upper() in reserved_keywords or space_pattern.search(field_name) is not None:
            field_with_type += '`' + field_name + '`'
            fields_str += '`' + field_name + '`,'
        else:
            field_with_type += field_name
            fields_str += field_name + ','

        values_str += '%s,' + ' '

        if i[2] == u'CHAR':
            field_types[field_name] = u'TEXT'
            field_with_type += ' ' + u'TEXT' + ','
        else:
            field_types[field_name] = i[2]
            field_with_type += ' ' + i[2] + ','

    fields_str = fields_str[:-1]
    values_str = values_str[:-2]

    # TODO 在mysql中创建对应的表
    field_with_type = field_with_type[:-1]
    create_command = "create table {0} ({1}, {2}) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci".format(table_name, field_with_type, pk_of_table[table_name])
    try:
        mysql_cursor.execute(create_command)
    except pymysql.err.InternalError:
        print('{0}.Table {1} transferred successfully!\n'.format(index + 1, table_name))
        continue
    except pymysql.err.ProgrammingError:
        traceback.print_exc()
        print(create_command)
        for k, v in field_types.items():
            print(k, v)
        exit()

    # TODO 获取此表所有记录，将类型为char的字段值转为简体，存入mysql表中
    sqlite_db.row_factory = dict_factory
    sqlite_cursor = sqlite_db.cursor()
    records = sqlite_cursor.execute("select * from {0}".format(table_name)).fetchall()

    insert_command = "insert into {0} ({1}) values ({2})".format(table_name, fields_str, values_str)
    values_list = list()
    for record in records:
        values = list()
        for k, v in field_types.items():
            if (v.find('CHAR') != -1 or v.find('TEXT') != -1) and record[k] is not None and chinese_pattern.search(record[k]) is not None:
                values.append(tradition2simple(record[k]))
            else:
                values.append(record[k])

        # try:
        #     mysql_cursor.execute(insert_command, values)
        # except (pymysql.err.InternalError, pymysql.err.DataError):
        #     for v in values_list:
        #         print v
        #     print create_command
        #     print insert_command
        #     traceback.print_exc()
        #     exit()
        #
        # except pymysql.err.IntegrityError, e:
        #     # TODO 记录有duplicate key的表，查看是否是简繁转换造成的
        #     if table_name not in table_with_dk:
        #         table_with_dk[table_name] = e
        #     continue

        values_list.append(tuple(values))

    # mysql_db.commit()

    try:
        mysql_cursor.executemany(insert_command, values_list)
        mysql_db.commit()
    except (pymysql.err.InternalError, pymysql.err.DataError, pymysql.err.IntegrityError):
        for v in values_list:
            print(v)
        print(create_command)
        print(insert_command)
        traceback.print_exc()
        exit()

    print('{0}.Table {1} transferred successfully!\n'.format(index + 1, table_name))

name_of_table_without_PK = list()
for n in name_of_all_tables:
    if n not in name_of_table_with_PK:
        name_of_table_without_PK.append(n)

print('Total tables which doesn\'t contain PK: {0}'.format(len(name_of_table_without_PK)))
for index, table_name in enumerate(name_of_table_without_PK):
    print('{0}.Table {1} transferring...................'.format(index + 1, table_name))
    # TODO 还原sqlite的row factory
    sqlite_db.row_factory = row_factory
    sqlite_cursor = sqlite_db.cursor()

    # TODO 获取此表每个字段的类型
    field_types = OrderedDict()
    field_with_type = ''
    fields_str = ''
    values_str = ''
    for i in sqlite_cursor.execute("PRAGMA TABLE_INFO({0})".format(table_name)).fetchall():
        # TODO 给带空格的字段加下划线
        field_name = i[1]

        if field_name.upper() in reserved_keywords or space_pattern.search(field_name) is not None:
            field_with_type += '`' + field_name + '`'
            fields_str += '`' + field_name + '`,'
        else:
            field_with_type += field_name
            fields_str += field_name + ','

        values_str += '%s,' + ' '

        if i[2] == u'CHAR':
            field_types[field_name] = u'TEXT'
            field_with_type += ' ' + u'TEXT' + ','
        else:
            field_types[field_name] = i[2]
            field_with_type += ' ' + i[2] + ','

    fields_str = fields_str[:-1]
    values_str = values_str[:-2]

    # TODO 在mysql中创建对应的表
    field_with_type = field_with_type[:-1]
    create_command = "create table {0} ({1}) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci".format(table_name, field_with_type)
    try:
        mysql_cursor.execute(create_command)
    except pymysql.err.InternalError:
        print('{0}.Table {1} transferred successfully!\n'.format(index + 1, table_name))
        continue
    except pymysql.err.ProgrammingError:
        traceback.print_exc()
        print(create_command)
        for k, v in field_types.items():
            print(k, v)
        exit()

    # TODO 获取此表所有记录，将类型为char的字段值转为简体，存入mysql表中
    sqlite_db.row_factory = dict_factory
    sqlite_cursor = sqlite_db.cursor()
    records = sqlite_cursor.execute("select * from {0}".format(table_name)).fetchall()

    insert_command = "insert into {0} ({1}) values ({2})".format(table_name, fields_str, values_str)
    values_list = list()
    for record in records:
        values = list()
        for k, v in field_types.items():
            if (v.find('CHAR') != -1 or v.find('TEXT') != -1) and record[k] is not None and chinese_pattern.search(record[k]) is not None:
                values.append(tradition2simple(record[k]))
            else:
                values.append(record[k])

        # try:
        #     mysql_cursor.execute(insert_command, values)
        # except (pymysql.err.InternalError, pymysql.err.DataError):
        #     for v in values_list:
        #         print v
        #     print create_command
        #     print insert_command
        #     traceback.print_exc()
        #     exit()
        #
        # except pymysql.err.IntegrityError, e:
        #     # TODO 记录有duplicate key的表，查看是否是简繁转换造成的
        #     if table_name not in table_with_dk:
        #         table_with_dk[table_name] = e
        #     continue

        values_list.append(tuple(values))

    # mysql_db.commit()

    try:
        mysql_cursor.executemany(insert_command, values_list)
        mysql_db.commit()
    except (pymysql.err.InternalError, pymysql.err.DataError, pymysql.err.IntegrityError):
        for v in values_list:
            print(v)
        print(create_command)
        print(insert_command)
        traceback.print_exc()
        exit()

    print('{0}.Table {1} transferred successfully!\n'.format(index + 1, table_name))


# print 'Duplicate Table name with example error message:\n'
# for k, v in table_with_dk.items():
#     print k, v

# TODO 关闭数据库连接
mysql_db.close()
sqlite_db.close()