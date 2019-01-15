import requests
#http://docs.python-requests.org/en/master/ >> 공식사이트

r = requests.get('http://paullab.co.kr', auth=('user', 'pass'))
print (r.status_code)
print(r.encoding)
#print(r.text)
r.encoding = 'utf-8'
#print(r.text)
print(r.headers) #서버에 대한 정보
#print(r.json())

string = r.text.split(' ')
count = 0
for i in string:
    if i == 'facebook':
        count +=1
print(count)