import scrapy


class QuotesSpider(scrapy.Spider):
    name = "games2"
    start_urls = [
            'https://boardgamegeek.com/browse/boardgame'
    ]
    custom_settings = {'CLOSESPIDER_PAGECOUNT': 2}

            
    def parse(self, response):
        game_page_links = response.css('td:nth-child(3) a::attr(href')
        yield from response.follow_all(game_page_links, self.parse_game)
        
        page_links = response
        for quote in response.css('tr')[1:]:
            yield {
                'rank': quote.css('td:nth-child(1) *::text').getall()[-1].strip(),
                'image': quote.css('td:nth-child(2) img::attr(src)').get(),
                'title': quote.css('td:nth-child(3) a::text').get(),
                'year': quote.css('td:nth-child(3) span::text').get()[1:-1] if quote.css('td:nth-child(3) span::text').get() else '',
                'description': quote.css('td:nth-child(3) p::text').get().strip() if quote.css('td:nth-child(3) p::text').get() else '',
                'geek_rating': quote.css('td:nth-child(4) *::text').get().strip(),
                'avg_rating': quote.css('td:nth-child(5) *::text').get().strip(),
                'num_voters':quote.css('td:nth-child(6) *::text').get().strip()
            }
        next_page = "https://boardgamegeek.com" + response.css('div.fr a::attr(href)').getall()[-2]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
                        
    
'''
        #next_page = response.css('li.next a::attr(href)').get()
        #if next_page is not None:
            #next_page = response.urljoin(next_page)
        #yield scrapy.Request(next_page, callback=self.parse)
        
        'tags with #, classes with .'
'''