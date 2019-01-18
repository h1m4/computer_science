import requests as rq

import json

url = "http://www.example.com"

res = rq.post(url, data = json.dumps({"key1" : "value1", "key2" : "value2"}))

print(res.url)


#post를 요청할 때 데이터가 url에 포함되어 있지 않고 heade의 body에 포함되어 있어 추가적인 인자를 보내야 함
# 쿼리 스트링은 params를 이용하지만 body에 데이터를 추가할 때는 data를 이용함
#res.content : euc-kr로 되어있는 경우 content를 통해 가져오면 깨짐 현상을 방지할 수 있음
#res.text
