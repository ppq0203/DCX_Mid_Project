from bs4 import BeautifulSoup
from selenium import webdriver
# pip install selenium webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

import csv
import time

# 1. csv file open
# csv_name = "main_all.csv"
# csv_open = open(csv_name, "w+", encoding="utf-8")
# csv_writer = csv.writer(csv_open)
# csv_writer.writerow(("category", "drink", "image_url"))

# 2. Driver & BeautifulSoup
# driver = webdriver.Chrome(ChromeDriverManager().install()) # 설치가 안되어 있을 경우
driver = webdriver.Chrome()
# search = input()
crawling_url = "https://www.ssg.com/search.ssg?target=all&query=%EB%94%B8%EA%B8%B0kg" # " + search + "
driver.get(crawling_url)

# 3. Parsing html code
full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')  # DOM parser (mobile SAX parser -> sleep 필요없음)

time.sleep(3)

# elements = driver.find_element(By.XPATH, '//*[@id="item_unit_1000045118991"]/div[2]/div[3]/div[1]/em')
elements = driver.find_element(By.CLASS_NAME, '.cunit_t232')
# print(elements.get_attribute('innerHTML'))

# tr = []
# tr = driver.find_element(By.TAG_NAME, "tr")
# td_text = tr.get_attribute('td')
# tr[-3] = -3번째 td
# data = pd.DataFrame([tr[-3]])
