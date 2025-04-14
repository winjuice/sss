# 数据容器文件

import scrapy

class SpiderItem(scrapy.Item):
    pass

class YuanxiaoxinxiItem(scrapy.Item):
    # 学校名称
    schoolname = scrapy.Field()
    # 分类
    typename = scrapy.Field()
    # 学校类型
    typeschool = scrapy.Field()
    # 排名
    ranking = scrapy.Field()
    # 硕士类型
    degreename = scrapy.Field()
    # 专业名称
    specialname = scrapy.Field()
    # 专业编码
    specialcode = scrapy.Field()
    # 年份
    year = scrapy.Field()
    # 总分
    total = scrapy.Field()
    # 政治
    politics = scrapy.Field()
    # 英语
    english = scrapy.Field()
    # 专业课一
    specialone = scrapy.Field()
    # 专业课二
    specialtwo = scrapy.Field()

