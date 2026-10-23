import scrapy

class MLNAMESGAMES(scrapy.Spider):
    name = "mlnames_games"
    start_urls = ["https://lista.mercadolivre.com.br/games"]

    def parse(self, response): #método parse #objeto response
        csv_file = open('mlnames_games.csv', 'w')

        game_names = response.css('span[class=main-title]::text').getall()

        for name in game_names:
            csv_file.write(name + '\n')

        csv_file.close()