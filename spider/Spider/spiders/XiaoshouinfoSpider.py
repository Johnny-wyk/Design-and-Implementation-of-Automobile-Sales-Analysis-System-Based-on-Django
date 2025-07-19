# # -*- coding: utf-8 -*-

# 数据爬取文件

import scrapy
import pymysql
import pymssql
from ..items import XiaoshouinfoItem
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
# 销售信息
class XiaoshouinfoSpider(scrapy.Spider):
    name = 'xiaoshouinfoSpider'
    spiderUrl = 'https://xl.16888.com/ev-202001-202410-{}.html'
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
            if self.table_exists(cursor, '933733lu_xiaoshouinfo') == 1:
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
            if self.table_exists(cursor, '933733lu_xiaoshouinfo') == 1:
                cursor.close()
                connect.close()
                self.temp_data()
                return
        list = response.css('div[class="xl-table-data"] table tr:nth-child(n+2)')
        for item in list:
            fields = XiaoshouinfoItem()

            if '(.*?)' in '''td:nth-child(2) a::text''':
                try:
                    fields["chexing"] = str( re.findall(r'''td:nth-child(2) a::text''', item.extract(), re.DOTALL)[0].strip())

                except:
                    pass
            else:
                try:
                    fields["chexing"] = str( self.remove_html(item.css('''td:nth-child(2) a::text''').extract_first()))

                except:
                    pass
            if '(.*?)' in '''td:nth-child(4) a::text''':
                try:
                    fields["changshang"] = str( re.findall(r'''td:nth-child(4) a::text''', item.extract(), re.DOTALL)[0].strip())

                except:
                    pass
            else:
                try:
                    fields["changshang"] = str( self.remove_html(item.css('''td:nth-child(4) a::text''').extract_first()))

                except:
                    pass
            if '(.*?)' in '''td:nth-child(5) a::text''':
                try:
                    fields["minprice"] = float( re.findall(r'''td:nth-child(5) a::text''', item.extract(), re.DOTALL)[0].strip().split(' - ')[0])
                except:
                    pass
            else:
                try:
                    fields["minprice"] = float( self.remove_html(item.css('td:nth-child(5) a::text').extract_first()).split(' - ')[0])
                except:
                    pass
            if '(.*?)' in '''td:nth-child(5) a::text''':
                try:
                    fields["maxprice"] = float( re.findall(r'''td:nth-child(5) a::text''', item.extract(), re.DOTALL)[0].strip().split(' - ')[1])
                except:
                    pass
            else:
                try:
                    fields["maxprice"] = float( self.remove_html(item.css('td:nth-child(5) a::text').extract_first()).split(' - ')[1])
                except:
                    pass
            detailUrlRule = item.css('div.lbBox a::attr(href)').extract_first()
            detailUrlRule ='https://xl.16888.com'+ detailUrlRule 
            if self.protocol in detailUrlRule or detailUrlRule.startswith('http'):
                pass
            elif detailUrlRule.startswith('//'):
                detailUrlRule = self.protocol + ':' + detailUrlRule
            elif detailUrlRule.startswith('/'):
                detailUrlRule = self.protocol + '://' + self.hostname + detailUrlRule
            else:
                detailUrlRule = self.protocol + '://' + self.hostname + '/' + detailUrlRule
            yield scrapy.Request(url=detailUrlRule, meta={'fields': fields},  callback=self.detail_parse, dont_filter=True)

    # 详情解析
    def detail_parse(self, response):
        fields = response.meta['fields']
        try:
            if '(.*?)' in '''td:nth-child(1)::text''':
                fields["tjtime"] = str( re.findall(r'''td:nth-child(1)::text''', response.text, re.S)[0].strip())

            else:
                if 'tjtime' != 'xiangqing' and 'tjtime' != 'detail' and 'tjtime' != 'pinglun' and 'tjtime' != 'zuofa':
                    fields["tjtime"] = str( self.remove_html(response.css('''td:nth-child(1)::text''').extract_first()))

                else:
                    try:
                        fields["tjtime"] = str( emoji.demojize(response.css('''td:nth-child(1)::text''').extract_first()))

                    except:
                        pass
        except:
            pass
        try:
            if '(.*?)' in '''td:nth-child(2)::text''':
                fields["mxiaoliang"] = int( re.findall(r'''td:nth-child(2)::text''', response.text, re.S)[0].strip())
            else:
                if 'mxiaoliang' != 'xiangqing' and 'mxiaoliang' != 'detail' and 'mxiaoliang' != 'pinglun' and 'mxiaoliang' != 'zuofa':
                    fields["mxiaoliang"] = int( self.remove_html(response.css('''td:nth-child(2)::text''').extract_first()))
                else:
                    try:
                        fields["mxiaoliang"] = int( emoji.demojize(response.css('''td:nth-child(2)::text''').extract_first()))
                    except:
                        pass
        except:
            pass
        try:
            if '(.*?)' in '''td:nth-child(3) a::text''':
                fields["dyxlpm"] = int( re.findall(r'''td:nth-child(3) a::text''', response.text, re.S)[0].strip())
            else:
                if 'dyxlpm' != 'xiangqing' and 'dyxlpm' != 'detail' and 'dyxlpm' != 'pinglun' and 'dyxlpm' != 'zuofa':
                    fields["dyxlpm"] = int( self.remove_html(response.css('''td:nth-child(3) a::text''').extract_first()))
                else:
                    try:
                        fields["dyxlpm"] = int( emoji.demojize(response.css('''td:nth-child(3) a::text''').extract_first()))
                    except:
                        pass
        except:
            pass
        try:
            if '(.*?)' in '''td:nth-child(4)::text''':
                fields["zcsfe"] = float( re.findall(r'''td:nth-child(4)::text''', response.text, re.S)[0].strip().replace('%',''))
            else:
                if 'zcsfe' != 'xiangqing' and 'zcsfe' != 'detail' and 'zcsfe' != 'pinglun' and 'zcsfe' != 'zuofa':
                    fields["zcsfe"] = float( self.remove_html(response.css('''td:nth-child(4)::text''').extract_first()).replace('%',''))
                else:
                    try:
                        fields["zcsfe"] = float( emoji.demojize(response.css('''td:nth-child(4)::text''').extract_first()).replace('%',''))
                    except:
                        pass
        except:
            pass
        try:
            if '(.*?)' in '''td:nth-child(5) a::text''':
                fields["zcspm"] = int( re.findall(r'''td:nth-child(5) a::text''', response.text, re.S)[0].strip())
            else:
                if 'zcspm' != 'xiangqing' and 'zcspm' != 'detail' and 'zcspm' != 'pinglun' and 'zcspm' != 'zuofa':
                    fields["zcspm"] = int( self.remove_html(response.css('''td:nth-child(5) a::text''').extract_first()))
                else:
                    try:
                        fields["zcspm"] = int( emoji.demojize(response.css('''td:nth-child(5) a::text''').extract_first()))
                    except:
                        pass
        except:
            pass
        try:
            if '(.*?)' in '''td:nth-child(6) a::text''':
                fields["zwxcpm"] = int( re.findall(r'''td:nth-child(6) a::text''', response.text, re.S)[0].strip())
            else:
                if 'zwxcpm' != 'xiangqing' and 'zwxcpm' != 'detail' and 'zwxcpm' != 'pinglun' and 'zwxcpm' != 'zuofa':
                    fields["zwxcpm"] = int( self.remove_html(response.css('''td:nth-child(6) a::text''').extract_first()))
                else:
                    try:
                        fields["zwxcpm"] = int( emoji.demojize(response.css('''td:nth-child(6) a::text''').extract_first()))
                    except:
                        pass
        except:
            pass
        return fields

    # 数据清洗
    def pandas_filter(self):
        engine = create_engine('mysql+pymysql://root:123456@localhost/spider933733lu?charset=UTF8MB4')
        df = pd.read_sql('select * from xiaoshouinfo limit 50', con = engine)

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
            insert into `xiaoshouinfo`(
                id
                ,chexing
                ,changshang
                ,minprice
                ,maxprice
                ,tjtime
                ,mxiaoliang
                ,dyxlpm
                ,zcsfe
                ,zcspm
                ,zwxcpm
            )
            select
                id
                ,chexing
                ,changshang
                ,minprice
                ,maxprice
                ,tjtime
                ,mxiaoliang
                ,dyxlpm
                ,zcsfe
                ,zcspm
                ,zwxcpm
            from `933733lu_xiaoshouinfo`
            where(not exists (select
                id
                ,chexing
                ,changshang
                ,minprice
                ,maxprice
                ,tjtime
                ,mxiaoliang
                ,dyxlpm
                ,zcsfe
                ,zcspm
                ,zwxcpm
            from `xiaoshouinfo` where
                `xiaoshouinfo`.id=`933733lu_xiaoshouinfo`.id
            ))
            order by rand()
            limit 50;
        '''

        cursor.execute(sql)
        connect.commit()
        connect.close()
