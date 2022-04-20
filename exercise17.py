import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
r_html = r.text
# print(r_html)

soup = BeautifulSoup(r_html, 'html.parser')

for titles in soup.find_all(class_="story_wrapper indicate-hover css-18cyl96"):
	title = titles.a
	print(title.string)

# r = requests.get(baseurl)
# soup = BeautifulSoup(r.text, 'html.parser')

# posts = soup.select('section:not(section[data-testid="block-Briefings"]) article')

# for i, post in enumerate(posts, 1):
#     print('{: <4}{}'.format(str(i) + '.', post.find('h2').text))