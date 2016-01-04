# -*- coding: utf-8 -*-
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from cafe.items import CafeItem
from cafe.utils import clean_str, list_to_clean_str

DOMAIN = 'www.lacolombe.com'
BASE_URL = 'http://%s/pages/coffee' % DOMAIN


class LaColombeSpider(CrawlSpider):
    name = 'lacolombe'
    allowed_domains = [DOMAIN]
    start_urls = [BASE_URL]
    allowed_pages = re.compile('/collections/')

    rules = (
        Rule(LinkExtractor(allow=allowed_pages), callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        self.logger.debug('Parsing reponse from %s', response.url)
        i = CafeItem()
        i['url'] = response.url
        i['brand'] = 'La Colombe'
        i['name'] = clean_str(response.xpath(
            '//h1[@itemprop="name"]/text()').extract()[0])
        i['size'] = '12 oz'
        i['description'] = list_to_clean_str(response.xpath(
            '//div[@itemprop="description"]//text()').extract())
        i['image'] = response.xpath(
            '//div[@id="ProductPhoto"]/img/@src').extract()[0]
        i['price'] = clean_str(response.xpath(
            '//span[@id="ProductPrice"]/text()').extract()[0])
        return i
