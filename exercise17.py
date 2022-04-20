import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.nytimes.com/'

r = requests.get(baseurl)
soup = BeautifulSoup(r.text, 'html.parser')

posts = soup.select('section:not(section[data-testid="block-Briefings"]) article')

for i, post in enumerate(posts, 1):
    print('{: <4}{}'.format(str(i) + '.', post.find('h2').text))