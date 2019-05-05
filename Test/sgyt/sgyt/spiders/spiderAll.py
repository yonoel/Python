import scrapy


class QuotesSpider(scrapy.Spider):
    name = "all"
    start_urls = [
        'http://www.cplusplus.com/reference/',
    ]

    def parse(self, response):
        pages = response.css("dl.links dt a").getall()
        self.savePageInHtml(self,response)
        for next_page in pages:
            next_page = next_page.split("\"")[1]
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parseChildNode)

    def parseChildNode(self,response):
        pages = response.css("dl.links dt a").getall()
        for next_page in pages:
            next_page = next_page.split("\"")[1]
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.savePageInHtml)

    def savePageInHtml(self, response):
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)