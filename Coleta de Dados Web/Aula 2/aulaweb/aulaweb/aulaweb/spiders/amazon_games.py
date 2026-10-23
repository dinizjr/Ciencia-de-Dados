import scrapy

class AmazonGamesSpider(scrapy.Spider):
    name = "amazon_games"
    start_urls = ["https://www.amazon.com.br/games"]

    def parse(self, response): #método parse #objeto response
        csv_file = open('amazon_games.csv', 'w')

        game_names = response.css('h2::text').getall()

        for name in game_names:
            csv_file.write(name + '\n')

        csv_file.close()