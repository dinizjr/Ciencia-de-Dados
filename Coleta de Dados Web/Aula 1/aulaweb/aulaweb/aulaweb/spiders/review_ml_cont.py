import scrapy
from scrapy import Selector
import csv

# grava a primeira página, depois chama a segunda e volta na gravação, mas como o padrão é diferente
# precisa parsear a segunda página também

class AmazonGamesSpider(scrapy.Spider):
    name = "review_ml_cont"
    start_urls = ["https://lista.mercadolivre.com.br/games"]

    def parse(self, response):  # método parse #objeto response
        #csv_file = open('review_ml_cont.csv', 'w')

        hxs = Selector(response)

        divs = hxs.select('//div[@class="item__info item__info--with-reviews"]')

        for i, div in enumerate(divs):

            name = div.select('.//span[contains(@class, "main-title")]/text()').get()
            symbol = div.select('.//span[contains(@class, "price__symbol")]/text()').get()
            price = div.select('.//span[contains(@class, "price__fraction")]/text()').get()
            dec = div.select('.//span[contains(@class, "price__decimals")]/text()').get()
            reviews = div.select('.//div[contains(@class, "item__reviews-total")]/text()').get()
            
            #if name is None or price is None:
                #continue
            if dec is None:
                dec = '00'
                
            prices = symbol +' '+ price +','+ dec
            
            content = ['%s;%s;%s\n' % (name, prices, reviews)]
            header = ['Produtos','Preço','Comentários']
            with open('review_ml_cont.csv', 'w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=header)
                writer.writeheader()
                writer.writerows(content)

            
            #csv_file.write('%s;%s;%s\n' % (name, prices, reviews))

        #csv_file.close()

        next_url = response.xpath('//a[@class="andes-pagination__link prefetch"]/@href').get()

        if not next_url is None:
            yield response.follow(next_url, callback=self.parseNextPage)

    def parseNextPage(self, response):  # método parse #objeto response

        #csv_file = open('review_ml_cont.csv', 'a')

        hxs = Selector(response)

        divs = hxs.select('//div[@class="item__info item__info--with-reviews"]')

        for i, div in enumerate(divs):

            name = div.select('.//span[contains(@class, "main-title")]/text()').get()
            symbol = div.select('.//span[contains(@class, "price__symbol")]/text()').get()
            price = div.select('.//span[contains(@class, "price__fraction")]/text()').get()
            dec = div.select('.//span[contains(@class, "price__decimals")]/text()').get()
            reviews = div.select('.//div[contains(@class, "item__reviews-total")]/text()').get()
            
            #if name is None or price is None:
                #continue
            if dec is None:
                dec = '00'
                
            prices = symbol +' '+ price +','+ dec
            

            content = ['%s;%s;%s\n' % (name, prices, reviews)]
            header = ['Produtos','Preço','Comentários']
            with open('review_ml_cont.csv', 'a', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=header)
                writer.writeheader()
                writer.writerows(content)

            
            #csv_file.write('%s;%s;%s\n' % (name, prices, reviews))

        #csv_file.close()

        next_url = response.xpath('//a[@class="andes-pagination__link prefetch"]/@href').get()

        if not next_url is None:
            yield response.follow(next_url, callback=self.parseNextPage)
