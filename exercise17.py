import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.nytimes.com/'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
response=requests.get(baseurl,headers=headers)
soup=BeautifulSoup(response.content,'html.parser')
print(response)

# r = requests.get(baseurl)
# soup = BeautifulSoup(r.text, 'html.parser')

# posts = soup.select('section:not(section[data-testid="block-Briefings"]) article')

# for i, post in enumerate(posts, 1):
#     print('{: <4}{}'.format(str(i) + '.', post.find('h2').text))