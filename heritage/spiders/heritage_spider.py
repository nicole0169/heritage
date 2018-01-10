import scrapy


class HeritageSpider(scrapy.Spider):

    name = "heritage"

    def start_requests(self):
        urls = ['http://whc.unesco.org/en/list/570/', 'http://whc.unesco.org/en/list/569/', ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = './pages/heritage-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
