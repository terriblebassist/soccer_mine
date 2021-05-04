# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Player(scrapy.Item):
    name = scrapy.Field()
    rating = scrapy.Field()
    profile = scrapy.Field()
    teams = scrapy.Field()
    country = scrapy.Field()
    skills = scrapy.Field()
    link = scrapy.Field()