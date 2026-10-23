import scrapy
#grava a primeira página, depois chama a segunda e volta na gravação, mas como o padrão é diferente
#precisa parsear a segunda página também

class AmazonGamesSpider(scrapy.Spider):
    name = "nextpages_ml"
    start_urls = ["https://lista.mercadolivre.com.br/games"]

    def parse(self, response): #método parse #objeto response
        csv_file = open('nextpages_ml.csv', 'w')

        game_names = response.xpath('//span[@class="main-title"]/text()').getall()

        for name in game_names:
            csv_file.write(name + '\n')

        csv_file.close()

        next_url = response.xpath('//a[@class="andes-pagination__link prefetch"]/@href').get()


        if not next_url is None:
            yield response.follow(next_url,
                                       callback=self.parseNextPage)

    def parseNextPage(self, response):  # método parse #objeto response

        '''import os
        exists = os.path.isfile('C:/Users/183134/Desktop/aulaweb/aulaweb/nextpages_ml.csv')

        if exists:
            csv_file = open('nextpages_ml.csv', 'a')
        else:

            csv_file = open('nextpages_ml.csv', 'w')'''

        csv_file = open('nextpages_ml.csv', 'a')

        game_names = response.xpath('//span[@class="main-title"]/text()').getall()

        for name in game_names:
            csv_file.write(name + '\n')

        csv_file.close()

        next_url = response.xpath('//a[@class="andes-pagination__link prefetch"]/@href').get()

        if not next_url is None:
            yield response.follow(next_url,
                                    callback=self.parseNextPage)