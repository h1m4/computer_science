from selenium import webdriver

url = 'https://pjt3591oo.github.io/'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

selected_id = driver.find_element_by_id('nav-trigger')
print(selected_id)
print(selected_id.tag_name)
print(selected_id.text)
