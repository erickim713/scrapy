import scrapy
import json

class SecondSpider(scrapy.Spider):
    name = "second"
    start_urls = []
    def __init__(self, filename = None):
        if filename:
            with open(filename, 'r') as f:
                data = json.load(f)
            baseURL = "https://www.rocketpunch.com"
            for entry in data:
                print(entry['company_url'])
                self.start_urls.append(baseURL + entry['company_url'])


    def parse(self, response):
        # 진행 중인 채용 정보
        
        # section for lists holding information to be included
        job_available = [] #list of job availables
        company_infocard = {"date-created": None, "member-count": None, "location": None, "homepage": None, "SNS": None}

        # section keys to be included
        job_key = "job_available"
        company_info = "company_info"
        url = 'url'


        for jobEntry in response.css('div.small-job-card.item'):
            # default setting for job card
            job_description = {"job-title": None, "job-stat": None, "specialties": None} 
            job_description['job-title'] = jobEntry.css('div.nowrap.content > div.ui.job-title.header > a.ui.primary.link::text').extract_first() #job title #직업 타이틀
            job_description['job-stat'] = jobEntry.css('div.nowrap.content > p.nowrap.job-stat-info::text').extract_first() #job information (pay) #직업 정보 (페이)
            job_description['specialties'] = jobEntry.css('div.nowrap.content > p.nowrap.job-specialties::text').extract_first() #skills needed for the job #직업에 필요한 고유 기술
            job_available.append(job_description)

        for com_info_entry in response.css('section#company-info.row > div.ui.top.attached.segment > div.ui.divided.company.info.items > div.item'):
            if(com_info_entry.css('div.title > i.ic-rocket.icon')): #date created
                company_infocard['date-created'] = com_info_entry.css('div.content::text').extract_first()
            elif(com_info_entry.css('div.title > i.ic-globe.icon')): #homepage url
                company_infocard['homepage'] = com_info_entry.css('div.content > a::attr(href)').extract_first()
            elif(com_info_entry.css('div.title > i.ic-location.icon')): #location just take the first location if provided
                company_infocard['location'] = com_info_entry.css('div.content > div.office.item::text').extract_first()
            elif(com_info_entry.css('div.title > i.ic-email_new.icon')): #SNS just take the first sns information if provided
                company_infocard['SNS'] = com_info_entry.css('div.sns.content > a::attr(href)').extract_first()
            elif(com_info_entry.css('div.title > i.ic-group.icon')): #member count
                company_infocard['member-count'] = com_info_entry.css('div.content > div.content::text').extract_first()


        #default setting for company card, for this section, the information is in the uniform format so i
        #am planning to distinguishing information by the icons used for each information.
        node = {}
        node.setdefault(job_key, job_available)
        node[company_info] = company_infocard
        node[url] = response.url



        yield node 
        # next_page = response.css('li.next a::attr("href")').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
        
        # in scrapy the found elements are returned as true while the unfound ones are returned false.
        
#
# scrape the inner pages by reading the csv and going through the pages:
# 	what information am i getting?
# 		-설립일
# 		-구성원숫자
# 		-위치
# 		-홈페이지 (okay)
# 		-SNS link 
# 		-채용정보: (done)
# 			-title (done)
# 			-분야 (done)
