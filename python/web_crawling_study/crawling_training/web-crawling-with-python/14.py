# 마우스제어

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://pjt3591oo.github.io/search'
driver = webdriver.Chrome('chromedriver')
driver.get(url)

driver.execute_script('alert("test")')
