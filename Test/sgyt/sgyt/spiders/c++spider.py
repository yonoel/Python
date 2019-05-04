# Walk-through of an example spider
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "c++spider"

    def start_requests(self):
        urls = [
            'http://www.cplusplus.com/reference/'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        self.log("--------------------")
        self.log(response)







