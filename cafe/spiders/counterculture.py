# -*- coding: utf-8 -*-
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from cafe.items import CafeItem

DOMAIN = 'counterculturecoffee.com'
BASE_URL = 'https://%s/store/coffee' % DOMAIN
URL_ARGS = '?dir=asc&limit=all&order=name'


class CounterCultureSpider(CrawlSpider):
    name = 'counterculture'
    allowed_domains = [DOMAIN]
    start_urls = [BASE_URL + URL_ARGS]
    allowed_pages = re.compile('^' + BASE_URL + '/')

    rules = (
        Rule(LinkExtractor(allow=allowed_pages), callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        self.logger.debug('Parsing reponse from %s', response.url)
        i = CafeItem()
        i['url'] = response.url
        i['name'] = response.xpath(
            '//div[@class="product-name"]/h1/text()').extract()
        i['description'] = response.xpath(
            '//div[@id="accordion"]/div/div/text()').extract()
        return i
