from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
header ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 "
                 "Safari/537.36",
    "Accept-Language":"en-IN,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,en-GB;q=0.6,en-US;q=0.5"
}
response = requests.get("https://internshala.com/internships/keywords-python/",headers=header)
soup = BeautifulSoup(response.text,'html.parser')
job_list= soup.find_all(class_="heading_4_5")
job_list = job_list[5:]
job_name = [job.text for job in job_list]
translator = str.maketrans({chr(10):'',chr(9):''})
for i in range(0,len(job_name)):
    job_name[i]= job_name[i].translate(translator)
company_list = soup.find_all(class_="company_and_premium")
company_name=[company.text for company in company_list]
for i in range(len(company_name)):
    company_name[i] = company_name[i].translate(translator).strip()
job_url = soup.find_all(class_="heading_4_5")
job_url = job_url[5:]
job_listing_link = [url.get("href") for url in job_url]

print(job_listing_link)

