# -*- coding: utf-8 -*-
import unittest
from tests.responses.file_response import response_from_file


class SpiderTest(unittest.TestCase):
    url = ''
    spider_name = ''
    name = ''
    brand = ''
    description = ''
    image = ''
    price = ''
    size = ''

    spider = None

    def _test_item(self, item):
        self.assertNotEqual(item['url'], '')
        self.assertEqual(item['url'], self.url)
        self.assertEqual(item['name'], self.name)
        self.assertEqual(item['brand'], self.brand)
        self.assertEqual(item['description'], self.description)
        self.assertEqual(item['image'], self.image)
        self.assertEqual(item['price'], self.price)
        self.assertEqual(item['size'], self.size)

    def _test_parse(self):
        filename = 'data/%s.html' % self.spider_name
        print 'Reading response from %s' % filename
        response = response_from_file(filename, self.url)
        results = self.spider.parse_item(response)
        self._test_item(results)
