import scrapy

class QuotesSpiderSpider(scrapy.Spider):
    name = 'spider_extract'
    dom_allowed = input("Enter allowed domain names: ")
    allowed_domains = [dom_allowed]
    dom_start = input("Enter start url: ")
    start_urls = [dom_start]

    def parse(self, response):
        quotes_dict = []
        selector = response.css('div.quoteDetails div.quoteText')

        for quote in selector:
            text = quote.css('::text').extract_first()
            author = quote.css('span::text').extract_first()
            combined = (text, author)
            quotes_dict += [combined]
        print(quotes_dict)
        self.write_as_html(quotes_dict)

    # write a html file
    def write_as_html(self, dict_items):
        html_text = '''
 Output:
 

         {LINKS}
     
 '''
 
        link_items = "____________________________START________________________________"
        for x in dict_items:
            link_items += f"""
Next->
{x[0]} {x[1]}"""
        link_items += "____________________________END________________________________"
        html_text = html_text.format(LINKS=link_items)
        
        with open("output.md", 'w') as fobj:
            fobj.write(html_text)