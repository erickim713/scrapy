import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.rocketpunch.com/jobs?career_type=4&q=&sort=ranking',
    ]

    def parse(self, response):
        for content in response.css('div.company-name'):
            yield {
                'company-name': content.css('a > h4.header.name > strong::text').extract_first()
                # 'author': quote.xpath('span/small/text()').extract_first(),
            }
        # next_page = response.css('li.next a::attr("href")').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
