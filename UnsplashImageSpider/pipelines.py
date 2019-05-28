# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib.request import urlopen
from settings import IMAGES_STORE


class UnsplashimagespiderPipeline(object):
    def process_item(self, item, spider):
        image_url = item['download'] + '?force=true'
        try:
            with urlopen(image_url) as result:
                data = result.read()
                with open(IMAGES_STORE + '\\' + item['image_id'] + '.jpg', 'wb+') as f:
                    f.write(data)
        except Exception as e:
            print('下载图片失败:', item['image_id'])
        return item
