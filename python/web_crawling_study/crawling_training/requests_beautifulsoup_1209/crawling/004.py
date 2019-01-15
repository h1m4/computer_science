from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
#html_doc를 parser로 잘라서 soup로 사용
#print(soup.prettify())
print(soup.title)
print(soup.p)
print(soup.h1)
print(soup.a)

print(soup.title.string)
print(soup.p.string)
#print(soup.h1.string)
print(soup.a.string)

#print(type(soup))
#print(dir(soup))

soup.find_all('a')
soup.find(id="link3")