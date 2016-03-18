import scrapy
from scrapy.selector import Selector

class ZillowSpider(scrapy.Spider):
    name = "zillow"
    allowed_domains = ["zillow.com"]
    start_urls = [
        "http://www.zillow.com/homes/for_sale/Honolulu-HI/"
    ]

    def parse(self, response):
        #instantiate selector with body of html page
        sel = Selector(response)

        #select all links to properties listed on the page
        links = sel.xpath("//a[contains(@class,'hdp-link routable')]/@href").extract()

        #append 'zillow.com' to the links, as they are incomplete
        #print all links
        for link in links:
            ret = "zillow.com" + link
            link = ret
            print link

        
