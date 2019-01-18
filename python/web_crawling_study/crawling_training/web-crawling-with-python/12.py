# 마우스제어

from selenium import webdriver

url = 'https://pjt3591oo.github.io/search'
driver = webdriver.Chrome('chromedriver')
driver.get(url)

selected_tag_a = driver.find_element_by_css_selector('input#search-box')
selected_tag_a.send_keys('test')
