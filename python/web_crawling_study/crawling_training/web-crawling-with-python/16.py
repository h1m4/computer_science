# 메시지 전달
from slackclient import SlackClient
from bs4 import BeautifulSoup
import requests as rq

def notification(message):
    slack_token = '발급받은 토큰'
    sc = SlackClient(slack_token)
    sc.api_call(
        "chat.postMessage",
        channel="#general",  # {#채널}의 형태로 채널 지정
        text=message
    )

base_url = 'https://pjt3591oo.github.io/'

res = rq.get(base_url)
soup = BeautifulSoup(res.content, 'lxml')

posts = soup.select('body main.page-content div.wrapper div.home div.p')

result = []

for post in posts:
    title = post.find('h3').text.strip()
    descript = post.find('h4').text.strip()
    author = post.find('span').text.strip()
    result.append(title)
    print(title, descript, author)

notification('%d개의 데이터 수집 완료'%len(result))
