# -*- coding: utf-8 -*-

import scrapy


class CafeItem(scrapy.Item):
    url = scrapy.Field()
    brand = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    image = scrapy.Field()
    price = scrapy.Field()
