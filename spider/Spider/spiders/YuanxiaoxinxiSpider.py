# # -*- coding: utf-8 -*-

# 数据爬取文件

import scrapy
import pymysql
import pymssql
from ..items import YuanxiaoxinxiItem
import time
from datetime import datetime,timedelta
import datetime as formattime
import re
import random
import platform
import json
import os
import urllib
from urllib.parse import urlparse
import requests
import emoji
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from selenium.webdriver import ChromeOptions, ActionChains
from scrapy.http import TextResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# 院校信息
class YuanxiaoxinxiSpider(scrapy.Spider):
    name = 'yuanxiaoxinxiSpider'
    spiderUrl = 'https://api.kaoyan.cn/pc/school/schoolList'
    start_urls = spiderUrl.split(";")
    protocol = ''
    hostname = ''
    realtime = False


    def __init__(self,realtime=False,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.realtime = realtime=='true'

    def start_requests(self):

        plat = platform.system().lower()
        if not self.realtime and (plat == 'linux' or plat == 'windows'):
            connect = self.db_connect()
            cursor = connect.cursor()
            if self.table_exists(cursor, 'do3uy2w0_yuanxiaoxinxi') == 1:
                cursor.close()
                connect.close()
                self.temp_data()
                return
        pageNum = 1 + 1

        for url in self.start_urls:
            if '{}' in url:
                for page in range(1, pageNum):

                    next_link = url.format(page)
                    yield scrapy.Request(
                        url=next_link,
                        callback=self.parse
                    )
            else:
                yield scrapy.Request(
                    url=url,
                    callback=self.parse
                )

    # 列表解析
    def parse(self, response):
        _url = urlparse(self.spiderUrl)
        self.protocol = _url.scheme
        self.hostname = _url.netloc
        plat = platform.system().lower()
        if not self.realtime and (plat == 'linux' or plat == 'windows'):
            connect = self.db_connect()
            cursor = connect.cursor()
            if self.table_exists(cursor, 'do3uy2w0_yuanxiaoxinxi') == 1:
                cursor.close()
                connect.close()
                self.temp_data()
                return
        data = json.loads(response.body)
        try:
            list = data["data"]["data"]
        except:
            pass
        for item in list:
            fields = YuanxiaoxinxiItem()


            try:
                fields["schoolname"] = str(emoji.demojize(self.remove_html( item["school_name"] )))

            except:
                pass
            try:
                fields["typename"] = str(emoji.demojize(self.remove_html( item["type_name"] )))

            except:
                pass
            try:
                fields["typeschool"] = str(emoji.demojize(self.remove_html( item["type_school_name"] )))

            except:
                pass
            try:
                fields["ranking"] = int( item["rk_rank"])
            except:
                pass
            detailUrlRule = item["school_id"]

            if '["school_id"]'.startswith('http'):
                if '{0}' in '["school_id"]':
                    detailQueryCondition = []
                    detailUrlRule = '["school_id"]'
                    i = 0
                    while i < len(detailQueryCondition):
                        detailUrlRule = detailUrlRule.replace('{' + str(i) + '}', str(detailQueryCondition[i]))
                        i += 1
            else:
                detailUrlRule =item["school_id"]

            detailUrlRule ='https://static.kaoyan.cn/json/score/2023/'+ detailUrlRule+'/0/1.json'

            if detailUrlRule.startswith('http') or self.hostname in detailUrlRule:
                pass
            else:
                detailUrlRule = self.protocol + '://' + self.hostname + detailUrlRule
                fields["laiyuan"] = detailUrlRule
            yield scrapy.Request(url=detailUrlRule, meta={'fields': fields}, callback=self.detail_parse)

    # 详情解析
    def detail_parse(self, response):
        fields = response.meta['fields']
        try:
            if '(.*?)' in '''["degree_type_name"]''':
                fields["degreename"] = str( re.findall(r'''["degree_type_name"]''', response.text, re.S)[0].strip())

            else:
                if 'degreename' != 'xiangqing' and 'degreename' != 'detail' and 'degreename' != 'pinglun' and 'degreename' != 'zuofa':
                    fields["degreename"] = str( self.remove_html(response.css('''["degree_type_name"]''').extract_first()))

                else:
                    try:
                        fields["degreename"] = str( emoji.demojize(response.css('''["degree_type_name"]''').extract_first()))

                    except:
                        pass
        except:
            pass
        try:
            if '(.*?)' in '''["special_name"]''':
                fields["specialname"] = str( re.findall(r'''["special_name"]''', response.text, re.S)[0].strip())

            else:
                if 'specialname' != 'xiangqing' and 'specialname' != 'detail' and 'specialname' != 'pinglun' and 'specialname' != 'zuofa':
                    fields["specialname"] = str( self.remove_html(response.css('''["special_name"]''').extract_first()))

                else:
                    try:
                        fields["specialname"] = str( emoji.demojize(response.css('''["special_name"]''').extract_first()))

                    except:
                        pass
        except:
            pass
        try:
            if '(.*?)' in '''["special_code"]''':
                fields["specialcode"] = str( re.findall(r'''["special_code"]''', response.text, re.S)[0].strip())

            else:
                if 'specialcode' != 'xiangqing' and 'specialcode' != 'detail' and 'specialcode' != 'pinglun' and 'specialcode' != 'zuofa':
                    fields["specialcode"] = str( self.remove_html(response.css('''["special_code"]''').extract_first()))

                else:
                    try:
                        fields["specialcode"] = str( emoji.demojize(response.css('''["special_code"]''').extract_first()))

                    except:
                        pass
        except:
            pass
        try:
            if '(.*?)' in '''["year"]''':
                fields["year"] = int( re.findall(r'''["year"]''', response.text, re.S)[0].strip())
            else:
                if 'year' != 'xiangqing' and 'year' != 'detail' and 'year' != 'pinglun' and 'year' != 'zuofa':
                    fields["year"] = int( self.remove_html(response.css('''["year"]''').extract_first()))
                else:
                    try:
                        fields["year"] = int( emoji.demojize(response.css('''["year"]''').extract_first()))
                    except:
                        pass
        except:
            pass
        try:
            if '(.*?)' in '''["total"]''':
                fields["total"] = int( re.findall(r'''["total"]''', response.text, re.S)[0].strip())
            else:
                if 'total' != 'xiangqing' and 'total' != 'detail' and 'total' != 'pinglun' and 'total' != 'zuofa':
                    fields["total"] = int( self.remove_html(response.css('''["total"]''').extract_first()))
                else:
                    try:
                        fields["total"] = int( emoji.demojize(response.css('''["total"]''').extract_first()))
                    except:
                        pass
        except:
            pass
        try:
            if '(.*?)' in '''["politics"]''':
                fields["politics"] = int( re.findall(r'''["politics"]''', response.text, re.S)[0].strip())
            else:
                if 'politics' != 'xiangqing' and 'politics' != 'detail' and 'politics' != 'pinglun' and 'politics' != 'zuofa':
                    fields["politics"] = int( self.remove_html(response.css('''["politics"]''').extract_first()))
                else:
                    try:
                        fields["politics"] = int( emoji.demojize(response.css('''["politics"]''').extract_first()))
                    except:
                        pass
        except:
            pass
        try:
            if '(.*?)' in '''["english"]''':
                fields["english"] = int( re.findall(r'''["english"]''', response.text, re.S)[0].strip())
            else:
                if 'english' != 'xiangqing' and 'english' != 'detail' and 'english' != 'pinglun' and 'english' != 'zuofa':
                    fields["english"] = int( self.remove_html(response.css('''["english"]''').extract_first()))
                else:
                    try:
                        fields["english"] = int( emoji.demojize(response.css('''["english"]''').extract_first()))
                    except:
                        pass
        except:
            pass
        try:
            if '(.*?)' in '''["special_one"]''':
                fields["specialone"] = int( re.findall(r'''["special_one"]''', response.text, re.S)[0].strip())
            else:
                if 'specialone' != 'xiangqing' and 'specialone' != 'detail' and 'specialone' != 'pinglun' and 'specialone' != 'zuofa':
                    fields["specialone"] = int( self.remove_html(response.css('''["special_one"]''').extract_first()))
                else:
                    try:
                        fields["specialone"] = int( emoji.demojize(response.css('''["special_one"]''').extract_first()))
                    except:
                        pass
        except:
            pass
        try:
            if '(.*?)' in '''["special_two"]''':
                fields["specialtwo"] = int( re.findall(r'''["special_two"]''', response.text, re.S)[0].strip())
            else:
                if 'specialtwo' != 'xiangqing' and 'specialtwo' != 'detail' and 'specialtwo' != 'pinglun' and 'specialtwo' != 'zuofa':
                    fields["specialtwo"] = int( self.remove_html(response.css('''["special_two"]''').extract_first()))
                else:
                    try:
                        fields["specialtwo"] = int( emoji.demojize(response.css('''["special_two"]''').extract_first()))
                    except:
                        pass
        except:
            pass
        return fields

    # 数据清洗
    def pandas_filter(self):
        engine = create_engine('mysql+pymysql://root:123456@localhost/spiderdo3uy2w0?charset=UTF8MB4')
        df = pd.read_sql('select * from yuanxiaoxinxi limit 50', con = engine)

        # 重复数据过滤
        df.duplicated()
        df.drop_duplicates()

        #空数据过滤
        df.isnull()
        df.dropna()

        # 填充空数据
        df.fillna(value = '暂无')

        # 异常值过滤

        # 滤出 大于800 和 小于 100 的
        a = np.random.randint(0, 1000, size = 200)
        cond = (a<=800) & (a>=100)
        a[cond]

        # 过滤正态分布的异常值
        b = np.random.randn(100000)
        # 3σ过滤异常值，σ即是标准差
        cond = np.abs(b) > 3 * 1
        b[cond]

        # 正态分布数据
        df2 = pd.DataFrame(data = np.random.randn(10000,3))
        # 3σ过滤异常值，σ即是标准差
        cond = (df2 > 3*df2.std()).any(axis = 1)
        # 不满⾜条件的⾏索引
        index = df2[cond].index
        # 根据⾏索引，进⾏数据删除
        df2.drop(labels=index,axis = 0)

    # 去除多余html标签
    def remove_html(self, html):
        if html == None:
            return ''
        pattern = re.compile(r'<[^>]+>', re.S)
        return pattern.sub('', html).strip()

    # 数据库连接
    def db_connect(self):
        type = self.settings.get('TYPE', 'mysql')
        host = self.settings.get('HOST', 'localhost')
        port = int(self.settings.get('PORT', 3306))
        user = self.settings.get('USER', 'root')
        password = self.settings.get('PASSWORD', '123456')

        try:
            database = self.databaseName
        except:
            database = self.settings.get('DATABASE', '')

        if type == 'mysql':
            connect = pymysql.connect(host=host, port=port, db=database, user=user, passwd=password, charset='utf8')
        else:
            connect = pymssql.connect(host=host, user=user, password=password, database=database)
        return connect

    # 断表是否存在
    def table_exists(self, cursor, table_name):
        cursor.execute("show tables;")
        tables = [cursor.fetchall()]
        table_list = re.findall('(\'.*?\')',str(tables))
        table_list = [re.sub("'",'',each) for each in table_list]

        if table_name in table_list:
            return 1
        else:
            return 0

    # 数据缓存源
    def temp_data(self):

        connect = self.db_connect()
        cursor = connect.cursor()
        sql = '''
            insert into `yuanxiaoxinxi`(
                id
                ,schoolname
                ,typename
                ,typeschool
                ,ranking
                ,degreename
                ,specialname
                ,specialcode
                ,year
                ,total
                ,politics
                ,english
                ,specialone
                ,specialtwo
            )
            select
                id
                ,schoolname
                ,typename
                ,typeschool
                ,ranking
                ,degreename
                ,specialname
                ,specialcode
                ,year
                ,total
                ,politics
                ,english
                ,specialone
                ,specialtwo
            from `do3uy2w0_yuanxiaoxinxi`
            where(not exists (select
                id
                ,schoolname
                ,typename
                ,typeschool
                ,ranking
                ,degreename
                ,specialname
                ,specialcode
                ,year
                ,total
                ,politics
                ,english
                ,specialone
                ,specialtwo
            from `yuanxiaoxinxi` where
                `yuanxiaoxinxi`.id=`do3uy2w0_yuanxiaoxinxi`.id
            ))
            order by rand()
            limit 50;
        '''

        cursor.execute(sql)
        connect.commit()
        connect.close()
