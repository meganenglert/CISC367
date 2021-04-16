import scrapy


class QuotesSpider(scrapy.Spider):
    name = "games"
    start_urls = [
        'https://boardgamegeek.com/browse/boardgame',
    ]

    def parse(self, response):
        # I spent an hour trying to figure this line out on my own and couldn't so
        # https://botproxy.net/docs/how-to/scrapy-pull-data-from-table-rows/
        for game in response.xpath('//*[contains(@class,"table-responsive")]//tr'):
            yield {
                'rank': game.css('td.collection_rank::text').strip(),
                'title': game.css('.primary::text').get()
                #'year': game.css('span.smallerfont dull::text').get()[1:-1],
                #'description': game.css('p.smallefont dull::text').getall(),
            }
            
            
            

        #next_page = response.css('li.next a::attr(href)').get()
        #if next_page is not None:
            #next_page = response.urljoin(next_page)
        #yield scrapy.Request(next_page, callback=self.parse)
        
        '''tags with #, classes with .'''