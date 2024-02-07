# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RecettesItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    ingredients = scrapy.Field()
    instructions = scrapy.Field()
    astuce = scrapy.Field()

    pass
