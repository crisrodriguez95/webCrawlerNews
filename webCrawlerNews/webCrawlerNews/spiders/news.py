import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from webCrawlerNews.items import WebcrawlernewsItem


class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['http://news.ycombinator.com/']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.morelink',)),
             callback="parse_item",
             follow=True),)


    def parse_item(self, response):
        item_links = response.css('.title > .titlelink::attr(href)').extract()
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        points = response.css('td.subtext > .score::text').get().replace(' points','')    

        item = WebcrawlernewsItem()
        item['points'] = points   
        yield item
