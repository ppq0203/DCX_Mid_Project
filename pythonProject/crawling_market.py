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
search = input()
crawling_url = "https://www.ssg.com/search.ssg?target=all&query=" + search + "%271kg%27"
driver.get(crawling_url)

# 3. Parsing html code
full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')  # DOM parser (mobile SAX parser -> sleep 필요없음)

time.sleep(3)

list = driver.find_element(By.CLASS_NAME, 'cunit_thmb_lst.cunit_thmb_lst4.cunit_thmb_w1000')  # <ul>
elements = list.find_element(By.CLASS_NAME, 'cunit_t232')  # 한 항목 <li>
title = elements.find_element(By.CLASS_NAME, 'title')  # <li> 안 이름 정보 class clickable
titleNa = title.find_element(By.CLASS_NAME, 'clickable')
name = titleNa.find_element(By.CLASS_NAME, 'tx_ko')  # 이름 class 안 내용
print(name.text)
marketDiv = elements.find_element(By.CLASS_NAME, 'cunit_price')  # <li> 안 가격 정보 class
price = marketDiv.find_element(By.CLASS_NAME, 'ssg_price')  # 가격 class 안 금액
print(price.text)

# nameList = []
# priceList = []
# nameList.append(name)
# priceList.append(price)