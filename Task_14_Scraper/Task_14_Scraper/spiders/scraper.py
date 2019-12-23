import scrapy

class Extractor(scrapy.Spider):
    name = 'jokes'
    url = input("Enter start url")
    start_urls = ['https://icyphox.sh/blog/python-for-re-1/'
    ]

    def parse(self, response):
        for data in response.css("//div[@class='data-text]"):
            yield{
                'ext_text': data.css(".//div[@class='data-text]/p").extract_first()
            }

        next_page = response.css["//li[@class='next']/a/@href"].extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url = next_page_link, callback=self.parse)
