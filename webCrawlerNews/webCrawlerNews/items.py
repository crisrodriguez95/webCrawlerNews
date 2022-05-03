# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlernewsItem(scrapy.Item):
    # define the fields for your item here like:
    points = scrapy.Field()
    comments = scrapy.Field()
    url = scrapy.Field()
    pass
