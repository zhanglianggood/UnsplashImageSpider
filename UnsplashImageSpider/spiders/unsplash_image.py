# -*- coding: utf-8 -*-
import scrapy
import json
from UnsplashImageSpider.items import UnsplashimagespiderItem


class UnsplashImageSpider(scrapy.Spider):
    name = 'unsplash_image'
    allowed_domains = ['unsplash.com']
    url = 'https://unsplash.com/napi/photos?page={page}&per_page={per_page}'
    page = 1
    per_page = 10
    start_urls = [url.format(page=page, per_page=per_page)]

    def parse(self, response):
        item = UnsplashimagespiderItem()
        html = json.loads(response.text)
        for each_image in html:
            item['image_id'] = each_image['id']
            item['download'] = each_image['links']['download']
            yield item
        if self.page <= 2:
            self.page += 1
            yield scrapy.Request(self.url.format(page=self.page, per_page=self.per_page), self.parse)
        else:
            print("爬取完成")

