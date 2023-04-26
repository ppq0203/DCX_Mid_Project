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
# "https://www.starbucks.co.kr/menu/drink_list.do"
crawling_url = "https://www.kamis.or.kr/customer/price/knowhow/knowhow.do?action=standardList"
driver.get(crawling_url)

# 3. Parsing html code
full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')#DOM parser (mobile SAX parser -> sleep 필요없음)

time.sleep(3)

items = soup.select('.mt30')
for idx, item in enumerate(items, 1):
    if item.text == 'VIEW 더보기':
        print(items[idx])
        print(idx)
        driver.find_element(By.XPATH,"//*[@id='main_pack']/section[3]/div/div[2]/panel-list/div[1]/more-button/div/a").click()
        # driver.find_element("xpath",'/html/body/div[3]/div[2]/div/div[1]/section[3]/div/div[2]/panel-list/div[1]/more-button/div/a').click()
        full_html = driver.page_source
        break

soup = BeautifulSoup(full_html, 'html.parser')
time.sleep(3)

items = soup.select('.bx._svp_item')

# 4. Get element selector (1)
categories = soup.select('#mCSB_1_container > li')


# #5. Get element selector (2)
# for i in range(2, len(categories)+1):
#     element = driver.find_elements_by_xpath('//[@id="container"]/div[2]/div[2]/div/dl/dd[1]/div[1]/dl/dd[1]/ul/li[1]/dl/dd') # 여러개
#     element = driver.find_element_by_css_selector(f'#mCSB_1_container > li:nth-child({i})')# 첫번째 것
#     category_name = element.text
#     time.sleep(2)
#     element.click()
#
#     full_html = driver.page_source
#     soup = BeautifulSoup(full_html, 'html.parser')
#
#     titles = soup.select(f'#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd:nth-child(2) > div.product_list > dl > dd:nth-child({1}) > ul > li > dl > dt > a > img')
#
#     #6. print drink_title, image url
#     for i, title in enumerate(titles):
#         print('title: ', title['alt'])
#         print('original src: ', title['src'])
#         print('image_url: ', title['src'].split('/')[4:])
#         url = crawling_url + '/' + '/'.join(title['src'].split('/')[4:])
#
#         # if i == 0:

for e, item in enumerate(items, 1):
    # ad = item.select('.txt.elss')
    # # print(ad)
    # # print(item.get('href'))
    # if ad: # .text == 'namu.wiki'
    #     print('나무위키')
    #     continue

    title = item.select_one('.api_txt_lines.total_tit._cross_trigger')  # 블록안에 또 다른 데이터
    # print(title)
    print(f"<<<{e}>>>")  # f = format
    print(f"{title.text}")
    print(f"{title.get('href')}")  # href 속성 값 가져옴
