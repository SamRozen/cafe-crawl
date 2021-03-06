# -*- coding: utf-8 -*-
from spider_test import SpiderTest
from cafe.spiders.counterculture import CounterCultureSpider


class CouterCultureSpiderTest(SpiderTest):
    url = 'https://counterculturecoffee.com/store/coffee/apollo'
    spider_name = 'counterculture'
    name = 'Apollo'
    size = '12 oz bag'
    brand = 'Counter Culture'
    price = '$15.75'

    description = 'Story In the summer of 2010, we introduced Apollo as a "seasonal espresso" with the goal of creating an espresso-brewing-friendly coffee with the best possible coffees of the moment with less focus on trying to make it taste exactly the same all of the time-all the while using freshly harvested coffees. In the beginning, the idea of Apollo was somewhat radical, especially looking back on how cautiously we introduced the idea that it could be from a single origin "some day"-a concept which now seems so familiar to us as to be unremarkable. In light of our #AnyCoffeeAnyBrew campaign, we\'ve updated how we talk about Apollo-no more reference to "espresso" here-but some things remain the same. Apollo will always be clean and bright. Specific flavors (e.g. citrus, floral, honey, etc.) will change with the seasons, but the thing that will never change is the clarity of the coffee. Place As many coffee people know, Ethiopia is the indigenous birthplace of coffee, which is thought to have grown wild in the southwestern forests there for centuries. Ethiopia\'s coffee trees have cross-pollinated an unknown number of times, creating more genetic coffee diversity than all other producing countries combined. Ethiopia also has the longest-standing traditions of coffee culture and cultivation in the world. No other country celebrates coffee with such high regard. The reverence of the daily coffee ceremony is a cultural treasure and an incredibly important part of the fabric of Ethiopian social, familial, and even business life. Notes 100% Idido, Yirgachaffe, Ethiopia'

    image = "./counterculture_files/apollo.jpg"

    def setUp(self):
        self.spider = CounterCultureSpider()

    def test_parse(self):
        self._test_parse()
