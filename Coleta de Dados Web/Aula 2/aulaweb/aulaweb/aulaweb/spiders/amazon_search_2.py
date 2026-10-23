import scrapy
from scrapy import Request
from scrapy import Selector
from w3lib.url import add_or_replace_parameters
#com add_or_replace_parameters

class AmazonSearchSpider(scrapy.Spider):
    name = 'amazon_search_2'

    def start_requests(self):

        csv_file = open('amazon_search_2.csv', 'w')
        #url de busca: https://www.amazon.com.br/s
        #parâmetros: ?k=fifa+19&i=videogames

        first_url = 'https://www.amazon.com.br/s'

        pars = {
            'k': 'fifa 19',
            'i': 'videogames'
        }

        first_url = add_or_replace_parameters(first_url, pars)

        print(first_url)

        yield Request(first_url, callback=self.parse)#retorna generator

    def parse(self, response):

        csv_file = open('amazon_search_2.csv', 'a')

        hxs = Selector(response)

        divs = hxs.select('//div[@class="sg-row"]')

        for i, div in enumerate(divs):
            name = div.select('.//span[contains(@class,"a-text-normal")]/text()').get()
            price = div.select('.//span[contains(@class, "a-price")]/span[@class="a-offscreen"]/text()').get()

            if name is None or price is None:
                continue

            csv_file.write('%s;%s\n' % (name, price))

        csv_file.close()

        # Extraindo a url da próxima página
        next_url = response.xpath('//li[@class="a-last"]/a/@href').get()

        if not next_url is None:
            yield response.follow(next_url, callback=self.parse)
