import scrapy
# from scrapy.http import Response  # импортируется класс Response из scrapy.http.
# Это позволяет указать тип аргумента response в методе parse. Необязательный атрибут, улучшающий читаемость.


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    # allowed_domains = ["https://divan.ru"]
    # start_urls = ["https://www.divan.ru/category/divany-i-kresla"]
    #
    # def parse(self, response):
    #     divans = response.css('div._Ud0k')
    #     for divan in divans:
    #         yield {
    #             'name': divan.css('div.lsooF span::text').get(),
    #             'price': divan.css('div.pY3d2 span::text').get(),
    #             'url': divan.css('a').attrib['href']
    #         }
    allowed_domains = ['market-sveta.ru']
    start_urls = ['https://www.market-sveta.ru/category/ljustry-podvesnye/']

    def parse(self, response):
        lamps = response.css('div.product-item')
        for i, lamp in enumerate(lamps, start=1):
            name = lamp.css('div.name a::text').get()
            price = lamp.css('div.price.ys_p::text').get()
            url = lamp.css('a').attrib['href']
            name = name.strip() if name else None
            price = price.strip() if price else None
            url = url.strip() if url else None
            print(f"Lamp {i}: Name: {name}, Price: {price}, URL: {url}")
            yield {
                    'name': name,
                    'price': price,
                    'url': url
                }
