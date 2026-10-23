import scrapy

class MercadoLivreSpider(scrapy.Spider):
    name = "ml_games"
    #start_urls = ["https://www.amazon.com.br/games"]
    start_urls = ["https://lista.mercadolivre.com.br/games"]

    def parse(self, response): #método parse #objeto response
        html_file = open('ml_games.html', 'w')

        html_file.write(str(response.body))

        html_file.close()