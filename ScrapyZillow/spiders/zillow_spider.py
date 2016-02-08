import scrapy
from scrapy.selector import Selector

class ZillowSpider(scrapy.Spider):
    name = "zillow"
    allowed_domains = ["zillow.com"]
    start_urls = [
        "http://www.zillow.com/homes/for_sale/Honolulu-HI/"
    ]

    def parse(self, response):
        sel = Selector(response)
        prices = sel.xpath('//*[contains(concat(" ", normalize-space(@span), " "), " price ")]')
        items = []

        for price in prices:
            items.append(price)
            print price
        
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(items)
        