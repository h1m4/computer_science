# 메시지 전달
from slackclient import SlackClient
from bs4 import BeautifulSoup
import requests as rq

slack_token = '발급받은 토큰'
sc = SlackClient(slack_token)

def notification(message, sc):
    sc.api_call(
        "chat.postMessage",
        channel="#general",  # {#채널}의 형태로 채널 지정
        text=message
    )

def is_user(k):
    return 'type' in k and 'text' in k and 'user' in k

def is_receieve(data):
    return len(data)

if sc.rtm_connect():
    while True:
        receive_data = sc.rtm_read()
        if is_receieve(receive_data):
            keys = list(receive_data[0].keys())
            if is_user(keys):
                message = receive_data[0]['text']
                print(receive_data)
                notification(message + ' response', sc)
    time.sleep(1)
else:
    print("Connection is Failed")
