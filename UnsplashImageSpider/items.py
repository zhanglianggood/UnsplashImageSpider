# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UnsplashimagespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片id
    image_id = scrapy.Field()
    # 图片下载地址
    download = scrapy.Field()
