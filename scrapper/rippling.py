#import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import By method to find the elements
from selenium.webdriver.common.by import By
#import time library to give sleep time to load data(bcz if we try to extract the data before getting loaded then we may get errros)
import time
import csv
#basically selenium uses a bot for automation and it opens a browser window when run the code so to remove the window we have to import and set options
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
#importing requests
import requests
#importing beautifulsoup for scraping
from bs4 import BeautifulSoup
import time

firefox_options = Options()
#setting the --headless argument to stop the browser window from opening as selenium is a type of automated browser software it opens browser window when we run code
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(options=firefox_options)
#take the url of website
url = "https://www.rippling.com/careers/open-roles"
#this code gets the info from the url given
driver.get(url)
#this code is to wait till the data gets loaded from url
driver.implicitly_wait(10)
#we can execute javascript code using driver.execute_script here i used javascript to scroll down to bottom
driver.execute_script("window.scrollTo(0,0.95*document.body.scrollHeight);")
#waiting for some time to get the changes loaded
time.sleep(3)
final_data=[]

#getting the info of the html source code using beautiful soup and driver.page_source which gives the source code of html file
soup = BeautifulSoup(driver.page_source,"html.parser")
#finding all the job_positings divs
all_jobs = soup.find_all("a", class_="flex flex-col md:flex-row no-underline relative")
job_elements=[]
for job in all_jobs:
    # print(job.prettify())
    # print(job.find('p', class_='pl-16').text.strip())
    if job.find('p', class_='pl-16').text.strip()=='Engineering':
        job_elements.append(job)
        
# job_elements = field.find_all("a", class_="heading show")
# print(len(job_elements))
for i in job_elements:
    #getting info of all the job listings
    soup2 = BeautifulSoup(str(i),"html.parser")
    job_link = soup2.find("a")["href"]
    job_title = soup2.find("p", class_="pr-16").text
    # job_category = soup2.find("div",class_='col-span-4 py-4 text-sm lg:text-lg text-dark').text
    job_location = soup2.find("p", class_="pl-8").text
    final_data.append({"job_title":job_title,"job_location":job_location,"job_link":job_link})

#converting the data into json
json_data = json.dumps({"company":"rippling","data":final_data})
print(json_data)
#driver.quit()exits selenium
driver.quit()