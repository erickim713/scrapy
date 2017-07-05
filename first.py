import scrapy


# rocketpunch internships
class FirstSpider(scrapy.Spider):
    name = "first"
    start_urls = [
        'https://www.rocketpunch.com/jobs?career_type=4',
    ]
    def __init__(self):
        self.download_delay = 1

    def parse(self, response):
        for content in response.css('div.company.item'):
            yield {
                'company-name': content.css('div.content > div.company-name > a > h4.header.name > strong::text').extract_first(),
                'description': content.css('div.content > div.description::text').extract_first(),
                'company_url': content.css('div.content > div.company-name > a::attr(href)') .extract_first(),
            }

        next_page = response.css('div.tablet.computer.large.screen.widescreen.only > a.active.item + a::attr(data-query-add)').extract_first()
        next_page = self.start_urls[0] + "&" + next_page
        if next_page is not None:
            yield response.follow(next_page, self.parse)
