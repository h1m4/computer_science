from django.shortcuts import render
#from .models import Post
from bs4 import BeautifulSoup
import requests

r = requests.get('사이트 이름')
r.encoding = 'utf-8'
x = []

soup = BeautifulSoup(r.text, 'html.parser')
listNum = soup.select('.title_text')

for i, j in enumerate(listNum, 1):
    x.append([i, j.text.strip()])


def index(request):
    return render(request, 'main/index.html', {'x' : x})

# Create your views here.
