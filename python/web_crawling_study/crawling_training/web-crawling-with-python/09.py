from selenium import webdriver

url = 'https://pjt3591oo.github.io/'

driver = webdriver.Chrome('chromedriver')
driver.get(url)

selected_tag_p = driver.find_element_by_tag_name('p')
print(selected_tag_p)
print(selected_tag_p.tag_name)
print(selected_tag_p.text)


selected_tags_p = driver.find_element_by_tag_name('p')
print(selected_tags_p)
