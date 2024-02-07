import scrapy

class DessertSpider(scrapy.Spider):
    name = "dessert"
    allowed_domains = ["www.cuisineaz.com"]
    start_urls = ["https://www.cuisineaz.com/recettes/nappage-chocolat-blanc-81430.aspx", "https://www.cuisineaz.com/recettes/pate-a-tartiner-legere-117073.aspx", "https://www.cuisineaz.com/recettes/meringue-simple-59583.aspx"]

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
