import scrapy
from scrapy import Request
from scrapy import Selector
from w3lib.url import add_or_replace_parameters
# com construtor

class AmazonSearchSpider(scrapy.Spider):
    name = 'ml_search'

    def __init__(self, q='', cat=''):#construtor
        self.query = q
        self.category = cat

    def start_requests(self):

        csv_file = open('ml_search.csv', 'w')

        first_url = 'https://games.mercadolivre.com.br'

        first_url +=  '/%s/%s' % (self.category, self.query)

        print(first_url)

        yield Request(first_url, callback=self.parse)#retorna generator

    def parse(self, response):

        csv_file = open('ml_search.csv', 'a')

        hxs = Selector(response)

        divs = hxs.select('//div[contains(@class,"item__info ")]')
        #divs = hxs.select('//div[@class="item__info "]')

        for i, div in enumerate(divs):

            name = div.select('.//span[contains(@class, "main-title")]/text()').get()
            symbol = div.select('.//span[contains(@class, "price__symbol")]/text()').get()
            price = div.select('.//span[contains(@class, "price__fraction")]/text()').get()
            dec = div.select('.//span[contains(@class, "price__decimals")]/text()').get()
            reviews = div.select('.//div[contains(@class, "item__reviews-total")]/text()').get()

            if name is None or price is None:
                continue

            if dec is None:
                dec = '00'
            if reviews is None:
                reviews = '0'

            prices = symbol + ' ' + price + ',' + dec

            csv_file.write('%s;%s;%s\n' % (name, prices, reviews))

        csv_file.close()

        next_url = response.xpath('//a[@class="andes-pagination__link prefetch"]/@href').get()

        if not next_url is None:
            yield response.follow(next_url, callback=self.parse)


