# -*- coding: utf-8 -*-
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from cafe.items import CafeItem
from cafe.utils import clean_str, list_to_clean_str

DOMAIN = 'shop.parlorcoffee.com'
BASE_URL = 'http://%s/collections/frontpage' % DOMAIN


class ParlorSpider(CrawlSpider):
    name = 'parlor'
    allowed_domains = [DOMAIN]
    start_urls = [BASE_URL]
    allowed_pages = re.compile('^%s/products/' % BASE_URL)

    rules = (
        Rule(LinkExtractor(allow=allowed_pages), callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        i = CafeItem()
        i['url'] = response.url
        i['brand'] = 'Parlor Coffee'
        i['name'] = clean_str(response.xpath(
            '//h2[@itemprop="name"]/text()').extract()[0])
        desc = list_to_clean_str(response.xpath(
            '//span[@itemprop="description"]/p[1]//text()').extract())
        if len(desc) == 0:
            desc = list_to_clean_str(response.xpath(
                '//span[@itemprop="description"]//div//text()').extract())
        i['description'] = desc
        i['size'] = list_to_clean_str(response.xpath(
            '//span[@itemprop="description"]/p[2]//text()').extract())
        i['image'] = response.xpath(
            '//div[@class="image_about"]').extract()[0]
        i['price'] = clean_str(response.xpath(
            '//span[@class="single_product_price"]/text()').extract()[0])
        return i
