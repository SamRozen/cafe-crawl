# -*- coding: utf-8 -*-
from spider_test import SpiderTest
from cafe.spiders.lacolombe import LaColombeSpider


class LaColombeSpiderTest(SpiderTest):
    url = 'http://www.lacolombe.com/collections/darker/products/corsica'
    spider_name = 'lacolombe'
    name = 'Corsica'
    size = '12 oz'
    brand = 'La Colombe'
    price = '$12.00'

    description = 'Blend Notes Uncommon, Rich, Full. Corsica is blended and roasted for richness and possesses a long-lasting coffee finish. In a word, Corsica is bold! For those who love RICH coffee. Corsica is the quintessential filter coffee with a character all its own. Blend Ingredients Click on a country to find out more Available in 12 oz & 5 lb Ingredient Detail Origin : Brazil Region : Cerrado Minas COOP/FARM : Lacador We applaud our Brazilian partner\'s commitment to preserving the surrounding ecosystem by permanently setting aside thousands of hectares of untouched old growth rainforest. Ingredient Detail Origin : Colombia Region : Sierra Nevada COOP/FARM : Asoprokan Grown on the northeastern face of the Sierra Nevada de Santa Marta Mountains, the tallest seaside elevation in Colombian and is the work of the ASOPROKAN co-op, a collective instrumental in stabilizing the community while caring for its complex ecosystem. The farmers are indigenous Arthuaca and Kankuama people whom are deeply spiritual and communal and base their production on sustainable organic practices only. Ingredient Detail Origin : Honduras Region : Capucas COOP/FARM : COCAFCAL mycapucascoffee.com Produced by small collective of like minded farmers surrounding the village of Capucas - wholly dedicated to sustainability, coffee quality and "reducing poverty and increasing the quality of life in the rural communities of the western Honduras." Ingredient Detail Origin : Mexico Region : Hautusco COOP/FARM : La Laja cafelalaja.com.mx La Laja Estate- Hautusco area, in their words "La Laja exists thanks to the ecosystem... our respect and commitment to Nature is unconditional"'

    image = '<img src="//cdn.shopify.com/s/files/1/0056/4562/products/Corsica-web_6d787057-e047-4edc-a67a-45e0e93e053f_large.jpeg?v=1443649169" alt="Corsica" id="ProductPhotoImg">'

    def setUp(self):
        self.spider = LaColombeSpider()

    def test_parse(self):
        self._test_parse()
