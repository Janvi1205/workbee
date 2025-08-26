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
url = "https://www.hcltech.com/careers/Careers-in-india#job-openings"
#this code gets the info from the url given
driver.get(url)
#this code is to wait till the data gets loaded from url
driver.implicitly_wait(10)
time.sleep(3)
while True:
    try:
        elem = driver.find_element(By.XPATH,"//a[@title='Load more items']")
        driver.execute_script("arguments[0].click()",elem)
        time.sleep(3)
    except:
        break
soup = BeautifulSoup(driver.page_source,"html.parser")
jobs = soup.find_all("tr")
L=[]
count = 0
for i in jobs:
    if count!=0:
        count+=1
        soup2 = BeautifulSoup(str(i),"html.parser")
        # print(soup2)
        try:
            title = soup2.find("td",class_='views-field views-field-field-designation').text.replace("  "," ")
            link = "https://www.hcltech.com"+soup2.find("a")["href"]
            # link=''
            location = soup2.find("td",class_='views-field views-field-field-kenexa-jobs-location').text.replace(" ","")
            L.append({"job_title":title,"job_location":location,"job_link":link})
        except:
            pass
    else:
        count+=1
print(len(L))
print(L)
driver.quit()
