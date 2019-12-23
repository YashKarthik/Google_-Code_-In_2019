import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = 'spider_extract'
    allowed_domains = ['https://www.goodreads.com/']
    start_urls = ['https://www.goodreads.com/quotes/']

    def parse(self, response):
        quotes_dict = []
        selector = response.css('div.quoteDetails div.quoteText')

        for quote in selector:
            text = quote.css('::text').extract_first()
            author = quote.css('span::text').extract_first()
            combined = (text, author)
            quotes_dict += [combined]

        self.write_as_html(quotes_dict)

    # write a html file
    def write_as_html(self, dict_items):
        html_text = '''
 
         {LINKS}

 '''
 
        link_items = "<ol>"
        for x in dict_items:
            link_items += f"<li>{x[0]} <span>{x[1]}</span></li>"
        link_items += "</ol>"
        html_text = html_text.format(LINKS=link_items)
        
        with open("info.html", 'w') as fobj:
            fobj.write(html_text)