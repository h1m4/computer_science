# 마우스제어

from selenium import webdriver

url = 'https://pjt3591oo.github.io/'
driver = webdriver.Chrome('chromedriver')
driver.get(url)

selected_selector = driver.find_element_by_css_selector('div.home div.p a')
print(selected_selector.tag_name)
print(selected_selector.text)
selected_selector.click()

'''
css를 이용해 a태그를 전부 가져옴. 루프를 돌려 크릭하면 0번째 요소만 클릭 이동하고 다음 인덱스 접근 시 에러 발생함
이는 메인페이지에서 돔을 가져오고 다음 페이지로 넘어가면 메인 페이지에서 가져온 돔에 접근 불가능하기 때문
클릭을 통해 페이지 이동 하려고 하면 안됨

클릭 사용 시 페이지 변화가 없고 해당 페이지 내에서 데이터가 추가되는 용도에서만 사용해야 함
'''
