import scrapy


class CharacterSpider(scrapy.Spider):
    name = "characterspider"
    start_urls =[
      " https://fr.wikipedia.org/wiki/Catégorie:Personnage_d%27animation"    ]

    def parse(self, response):
        for link in response.css('mw-content-ltr li'):
            yield {
                'character': likn.css('a ::text').extract_first()
            }
