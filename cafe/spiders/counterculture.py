# -*- coding: utf-8 -*-
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from cafe.items import CafeItem
from cafe.utils import clean_str, list_to_clean_str

DOMAIN = 'counterculturecoffee.com'
BASE_URL = 'https://%s/store/coffee' % DOMAIN
URL_ARGS = '?dir=asc&limit=all&order=name'


class CounterCultureSpider(CrawlSpider):
    name = 'counterculture'
    allowed_domains = [DOMAIN]
    start_urls = [BASE_URL + URL_ARGS]
    allowed_pages = re.compile('^%s/' % BASE_URL)

    rules = (
        Rule(LinkExtractor(allow=allowed_pages), callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        self.logger.debug('Parsing reponse from %s', response.url)
        i = CafeItem()
        i['url'] = response.url
        i['brand'] = 'Counter Culture'
        i['name'] = clean_str(response.xpath(
            '//div[@class="product-name"]/h1/text()').extract()[0])
        i['description'] = list_to_clean_str(response.xpath(
            '//div[@id="accordion"]//text()').extract())
        i['image'] = response.xpath(
            '//p[@class="product-image"]/img').extract()[0]
        i['price'] = clean_str(response.xpath(
            '//span[@class="price"]/text()').extract()[0])
        return i
