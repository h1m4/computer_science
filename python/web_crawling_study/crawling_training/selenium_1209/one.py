#C > crawling > main.py
from selenium import webdriver

path = "C:/crawling/chromedriver.exe"

#조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다.
driver = webdriver.Chrome(path)

#webdriver가 google 페이지에 접속하도록 명령
driver.get('https://www.google.com')

#webdriver를 종료하며 창이 사라진다.
driver.close()
