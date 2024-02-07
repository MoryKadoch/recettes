import scrapy
import json
from recettes.items import RecettesItem

class DessertSpider(scrapy.Spider):
    name = "dessert"
    allowed_domains = ["www.cuisineaz.com"]
    start_urls =  json.load(open("./../../urls.json", "r"))

    def parse(self, response):
        item = RecettesItem()
        ingredients = []

        ingredient = response.css("#main_content > section.borderSection.ingredients > ul > li:not(:first-child)")

        for elem in ingredient:            
            ingredients.append({ "name": elem.css("span:first-of-type::text").get(), "img": elem.css("picture > source::attr(srcset)").get() })

        item["name"] = response.css("h1.recipe-title::text").get()
        item["ingredients"] = ingredients
        item["instructions"] = response.css("section.instructions > ul > li > p > span::text").extract()
        item["astuce"] = response.css("section.instructions > section p:not(:empty)::text").get()

        yield item
        pass
