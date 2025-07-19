# 数据容器文件

import scrapy

class SpiderItem(scrapy.Item):
    pass

class XiaoshouinfoItem(scrapy.Item):
    # 车型
    chexing = scrapy.Field()
    # 厂商
    changshang = scrapy.Field()
    # 最低售价（万元）	
    minprice = scrapy.Field()
    # 最高售价（万元）	
    maxprice = scrapy.Field()
    # 时间
    tjtime = scrapy.Field()
    # 月销量(辆)
    mxiaoliang = scrapy.Field()
    # 当月销量排名
    dyxlpm = scrapy.Field()
    # 占厂商份额（%）
    zcsfe = scrapy.Field()
    # 在厂商排名
    zcspm = scrapy.Field()
    # 在微型车排名
    zwxcpm = scrapy.Field()

