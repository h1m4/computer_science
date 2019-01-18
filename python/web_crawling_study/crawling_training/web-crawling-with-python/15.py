from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

url = 'https://pjt3591oo.github.io/search'

search_keysword = 'db'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

selected_tag_a = driver.find_element_by_css_selector('input#search-box')

selected_tag_a.send_keys(search_keysword)
selected_tag_a.send_keys(Keys.ENTER)

soup = BeautifulSoup(driver.page_source, 'lxml')
items = soup.select('ul#search-results li')

for item in items:
    title = item.find('a').text
    description = item.find('p').text
    print(title)
    print(description)
