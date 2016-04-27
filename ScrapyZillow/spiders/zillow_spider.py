import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ZillowSpider(CrawlSpider):
    name = "zillow"
    allowed_domains = ["zillow.com/"]
    start_urls = [
        "http://www.zillow.com/homes/for_sale/Honolulu-HI/"
    ]

    rules = [
        Rule(LinkExtractor(
            allow=['.*']),
            callback = 'parse',
            follow=True)
    ]

    def parse(self, response):
        #instantiate selector with body of html page
        sel = Selector(response)

        #select all links to properties listed on the page
        links = sel.xpath("//a[contains(@class,'hdp-link routable')]/@href").extract()

        #append 'zillow.com' to the links, as they are incomplete
        #print all links
        for link in links:
            ret = "http://zillow.com" + link
            link = ret
            #print link

        #gets the URL for next page by looking for the "next" button
        next_page = response.xpath('//a[contains(.//text(), \'Next\')]/@href').extract()
        next_url = "http://zillow.com" + next_page[0]
        print "next url is located here!", next_url
        return next_url
