#C > crawling > main.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:/crawling/chromedriver.exe"

#조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다.
driver = webdriver.Chrome(path)

#webdriver가 google 페이지에 접속하도록 명령
driver.get('주소')

id = driver.find_element_by_id("아이디 입력 id")
pw = driver.find_element_by_id("password 입력 id")

id.send_keys("id key")
pw.send_keys("password key")

pw.send_keys(Keys.ENTER)

con = driver.find_element_by_id("status_btn_new_container")
con.click()
#검색 입력 부분에 커서를 올리고
#검색 입력 부분에 다양한 명령을 내리기 위해 elem 변수에 할당한다.
#elem = driver.find_element_by_name("q")
#입력 부분에 default로 값이 있을 수 있어 비운다.
#elem.clear()

#검색어를  입력한다.
#elem.send_keys("Selenium")
#검색을 실행한다.
#elem.submit()
#chromedriver를 종료하며 창을 닫는다.
driver.close()
