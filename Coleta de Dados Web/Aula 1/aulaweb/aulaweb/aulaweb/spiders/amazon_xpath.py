import scrapy
#grava a primeira página, depois chama a segunda e volta na gravação, mas como o padrão é diferente
#precisa parsear a segunda página também

class AmazonGamesSpider(scrapy.Spider):
    name = "amazon_xpath"
    start_urls = ["https://www.amazon.com.br/games"]

    def parse(self, response): #método parse #objeto response
        csv_file = open('amazon_xpath.csv', 'w')

        game_names = response.xpath('//div[@class="s-item-container"]//h2/text()').getall()

        for name in game_names:
            csv_file.write(name + '\n')

        csv_file.close()

        next_url = response.xpath('//a[@id="pagnNextlink"]/@href').get()


        if not next_url is None:
            #next_url = response.urljoin(next_url)
            yield response.follow(next_url,
                                       callback=self.parseNextPage)

            #yield scrapy.Request(next_url,
                            #callback=self.parse)

            #response.xpath('//span[contains(@class,"a-text-normal")]/text()').getall()


            #response.xpath('//li[@class="a-last"]/a/@href').getall()

            #o a é uma tag

    def parseNextPage(self, response):  # método parse #objeto response
        csv_file = open('amazon_xpath.csv', 'a')#a = append

        game_names = response.xpath('//span[contains(@class,"a-text-normal")]/text()').getall()

        for name in game_names:
            csv_file.write(name + '\n')

        csv_file.close()

        next_url = response.xpath('//li[@class="a-last"]/a/@href').get()

        if not next_url is None:
            yield response.follow(next_url,
                                  callback=self.parseNextPage)