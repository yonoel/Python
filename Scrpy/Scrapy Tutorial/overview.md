#Scrapy Tutorial
#Creating a project
```
scrapy startproject tutorial

```
This will create a tutorial directory with the following contents:
```
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
```
#Our first Spider
Spiders are classes that you define and that Scrapy uses to scrape information 
from a website (or a group of websites). They must subclass scrapy.Spider and define the initial requests to make, optionally how to follow links in the pages,
 and how to parse the downloaded page content to extract data.
 
This is the code for our first Spider. 
Save it in a file named quotes_spider.py under the tutorial/spiders directory in your project:
```
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
```
+ name: identifies the Spider. It must be unique within a project,
 that is, you can’t set the same name for different Spiders.
 
+ start_requests(): must return an iterable of Requests
(you can return a list of requests or write a generator function)
which the Spider will begin to crawl from.
Subsequent requests will be generated successively from these initial requests.

+ parse(): a method that will be called to handle the response downloaded for each of the requests made.
The response parameter is an instance of TextResponse that holds the page content and
has further helpful methods to handle it.
The parse() method usually parses the response,
extracting the scraped data as dicts and also finding new URLs to follow and creating new requests (Request) from them
#How to run our spider
```
scrapy crawl quotes
```
This command runs the spider with name quotes that we’ve just added, that will send some requests for the quotes.toscrape.com domain. You will get an output similar to this:
# Extracting data
```
scrapy shell url
```

# quotes from all the pages in the website.
```
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

```

