import time
import pandas as pd
from bs4.builder import HTML
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get('http://www.google.com')
time.sleep(1)

search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(2)

# from bs4 import BeautifulSoup
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# divs = soup.select('.g')
# title_list = []; content_list = []
# for div in divs :
#     title = div.select_one('.LC20lb DKV0Md').get_text()
#     content = div.select_one('.aCOpRe').get_text()
#     print(title)
#     print(content)

# df = pd.DataFrame({
#     'title' : title_list, 'content' : content_list
#     })
# df.to_csv('google.csv', sep='|')

divs = driver.find_element_by_css_selector('.g')
title_list = []; content_list = []
for div in divs :
    title = divs.find_element_by_css_selector('.LC20lb DKV0Md').text
    content = divs.find_element_by_css_selector('.aCOpRe').text
    print(title)
    print(content)