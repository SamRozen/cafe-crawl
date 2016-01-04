# -*- coding: utf-8 -*-
from spider_test import SpiderTest
from cafe.spiders.parlor import ParlorSpider


class ParlorSpiderTest(SpiderTest):
    url = 'http://shop.parlorcoffee.com/collections/frontpage/products/kenya-ibutiti-peaberry'
    spider_name = 'parlor'
    name = 'Kenya Ibutiti Peaberry'
    size = '8 ounce bag. Whole bean.'
    brand = 'Parlor Coffee'
    price = '$16.00'

    description = "When we cupped through hoards of Kenyan coffee samples early this year, two coffees stood out as exceptional on the cupping tables - not just in the first screening, but again in the second, and again the third. Those two coffees hailed from William Murathe's Ibutiti Estate. The Peaberry from Ibutiti possesses the same complex fruited character as the Ibutiti we've offered thus far; and yet, to compare the two is to undermine the truly grand nature of this coffee. The Peaberry is incredibly juicy, with resonating flavors of white peach, plum, and sweetened strawberry which linger with a tongue-coating, buttery mouthfeel."

    image = u'background-image:url(\'//cdn.shopify.com/s/files/1/0277/7983/products/Kenya_Ibutiti_Peaberry_grande.jpg?v=1446232221\')'

    def setUp(self):
        self.spider = ParlorSpider()

    def test_parse(self):
        return self._test_parse()
