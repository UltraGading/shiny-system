from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv

# OPEN THE URL
start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# OPEN THE LINK WITH THE BROWSER
browser = webdriver.Chrome(r"C:\Users\Nirvighan\Downloads\chromedriver_win32\chromedriver")
browser.get(start_url)
time.sleep(10)

# FUNTION FOR ADDING AND SCRAPPING THE DATA

def scrape():
    headers = ["name", "light_years_from_earth", 'radius',"mass"]
    stars_data = []
    
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for tr_tag in soup.find_all("tr"):
        td_tags = tr_tag.find_all("td")
        temp_list = []
        for index, td_tag in enumerate(td_tags):
            if index == 0:
                temp_list.append(td_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(td_tag.contents[0])
                except:
                    temp_list.append("")
            stars_data.append(temp_list)
        
    with open(r"D:\PythonProjects\PRO_C127\data.csv", "a+") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)
scrape()
