# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class S1Item(scrapy.Item):
    name = 'mofan'
    start_urls = ['https://morvanzhou.github.io/', ]
    def parse(self, response):
        yield {
            'title': response.css('h1::tet').extract_first(default='Missing').strip().replace(""", """),
            'url': response.url
        }
        urls = response.css('a::attr(href)').re(r'^/.+?/$')
        for url in urls:
            yield response.follow(url, callback=self.parse)
