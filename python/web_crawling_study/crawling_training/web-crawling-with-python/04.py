#특정 페이지는 헤더의 user-agent가 비었거나 쿠키가 비어있을 경우 정상적으로 html을 출력하지 않을 수 있음
# 이럴 때 헤더나 쿠키를 직접 만들어서 .post()해야함

import requests as rq

url = "https://pjt3591oo.github.io/"

res = rq.get(url, params = {"key1" : "value1", : "key2" : "value2"})

print(res.url)
