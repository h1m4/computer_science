from slackclient import SlackClient
import requests as rq
from bs4 import BeautifulSoup
import time

slack_token = '발급받은 토큰'
sc = SlackClient(slack_token)

# 메시지 전달
def notification(message, sc):
    sc.api_call(
        "chat.postMessage",
        channel="#general",
        text=message
    )

# 유저가 보낸 메시지 인지 파이썬이 응답한 메시지인지 검사
def is_user(k):
    return 'type' in k and 'text' in k and 'user' in k

def is_receive(data):
    return len(data)

def crawler():
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

    return '\n'.join(result)
# RTM
if sc.rtm_connect():
    while True:
        receive_data = sc.rtm_read()
        if is_receive(receive_data):
            keys = list(receive_data[0].keys())
            if is_user(keys):
                message = receive_data[0]['text']
                print(message)
                if message == 'crawler': #crawler 라는 메세지를 받으면 crawler()의 결과가 slack()에 메세지로 post됨(message = d)
                    d = crawler()
                    notification(d, sc)
        time.sleep(1)
else:
    print("Connection Failed")
