import scrapy


# rocketpunch internships
class FirstSpider(scrapy.Spider):
    name = "first"
    start_urls = [
        'https://www.rocketpunch.com/jobs?career_type=4&q=&sort=',
    ]

    def parse(self, response):
        for content in response.css('div.company.item'):
            yield {
                'company-name': content.css('div.content > div.company-name > a > h4.header.name > strong::text').extract_first(),
                'description': content.css('div.content > div.description::text').extract_first(),
                'company_url': content.css('div.content > div.company-name > a::attr(href)') .extract_first(),
            }
        # next_page = response.css('li.next a::attr("href")').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
