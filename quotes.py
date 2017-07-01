import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.rocketpunch.com/jobs?career_type=4&q=&sort=ranking',
    ]

    def parse(self, response):
        for content in response.css('div.company.item'):
            yield {
            # company name, description of company, available spots
                'company-name': content.css('div.content > div.company-name > a > h4.header.name > strong::text').extract_first(),
                'description': content.css('div.content > div.description::text').extract_first(),
                # 'availability': content.css('div.content > div.company-jobs > div.company-job.transition.visible > span.nowrap.job-title').extract_first(),
                # 'job-info': content.css('div.content > div.company-jobs > div.company-job.transition.visible > span.job-stat-info').extract_first()
            }
        # next_page = response.css('li.next a::attr("href")').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
