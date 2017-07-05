import json
from pprint import pprint
baseURL = "https://www.rocketpunch.com"
with open('first.json') as data_file:
	data = json.load(data_file)
with open('second.json') as data_file2:
	data2 = json.load(data_file2)


for entry in data:

	print("회사:" + entry['company-name'])
	print("설명:" + entry['description'])
	print("회사 URL:" + entry['company_url'] +"\n")

	# 각 회사의 default 값
	dateCreated = ""
	homepage = ""
	location = ""
	SNS = ""
	memberCount = ""

	for jobs in data2:
		if(jobs['url'] == baseURL + entry['company_url']):
			jobList = ""
			for i in range(len(jobs['job_available'])):
				if(jobs['job_available'][i]['job-title'] != None):
					jobList = jobList + "job title: " + jobs['job_available'][i]['job-title'].strip() + "\n"
				if(jobs['job_available'][i]['job-stat'] != None):
					jobList = jobList + "job stat: " + jobs['job_available'][i]['job-stat'].strip() +"\n"
				if(jobs['job_available'][i]['specialties'] != None):
					jobList = jobList + "job needed specialties: " + jobs['job_available'][i]['specialties'].strip() + "\n"
				if(i < len(jobs['job_available'])-1):
					jobList = jobList + "\n"
			if(jobs['company_info']['date-created'] != None):
				dateCreated = jobs['company_info']['date-created'].strip()
			if(jobs['company_info']['homepage'] != None):
				homepage = jobs['company_info']['homepage'].strip()
			if(jobs['company_info']['location'] != None):
				location = jobs['company_info']['location'].strip()
			if(jobs['company_info']['SNS'] != None):
				SNS = jobs['company_info']['SNS'].strip()
			if(jobs['company_info']['member-count'] != None):
				memberCount = jobs['company_info']['member-count'].strip()
			break

	print("jobs available are:\n" + jobList)
	print("date created: " + dateCreated)
	print("homepage: " + homepage)
	print("location: " + location)
	print("SNS: " + SNS)
	print("Member Count: " + memberCount)


	print('------------------------------------------------------')
	

