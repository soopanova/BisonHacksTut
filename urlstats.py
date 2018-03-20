from bs4 import BeautifulSoup
import requests

content = requests.get('http://cnn.com').text
soup = BeautifulSoup(content, 'html.parser')
print('There are {} anchors'.format(len(soup.find_all('a'))))
print('There are {} link'.format(len(soup.find_all('link'))))
print('There are {} scripts'.format(len(soup.find_all('script'))))

for link in soup.find_all('a'):
    if 'https' in link.get('href') or 'http' in link.get('href'):
        print(link.get('href'))