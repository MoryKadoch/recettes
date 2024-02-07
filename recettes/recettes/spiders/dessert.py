import scrapy
import json

class DessertSpider(scrapy.Spider):
    name = "dessert"
    allowed_domains = ["www.cuisineaz.com"]
    start_urls =  json.load(open("/home/mory/recettes/urls.json", "r"))
    print(start_urls)

    def parse(self, response):
        recette_infos = {}
        ingredients = []

        ingredient = response.css("#main_content > section.borderSection.ingredients > ul > li:not(:first-child)")

        for item in ingredient:            
            ingredients.append({ "name": item.css("span:first-of-type::text").get(), "img": item.css("picture > source::attr(srcset)").get() })

        recette_infos["name"] = response.css("h1.recipe-title::text").get()
        recette_infos["ingredients"] = ingredients
        recette_infos["instructions"] = response.css("section.instructions > ul > li > p > span::text").extract()
        recette_infos["astuce"] = response.css("section.instructions > section p:not(:empty)::text").get()

        yield(recette_infos)
        pass
