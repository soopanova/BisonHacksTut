from bs4 import BeautifulSoup
import requests
import argparse

# Getting CLI arguments to find website to load up
parser = argparse.ArgumentParser()
parser.add_argument('--url', '-u', help="The url to lookup")
args = parser.parse_args()


content = requests.get(args.url).text
soup = BeautifulSoup(content, 'html.parser')
print('***Stats for {}***'.format(args.url))
print('There are {} anchors'.format(len(soup.find_all('a'))))
print('There are {} link'.format(len(soup.find_all('link'))))
print('There are {} scripts'.format(len(soup.find_all('script'))))

'''for link in soup.find_all('a'):
    if 'https' in link.get('href') or 'http' in link.get('href'):
        print(link.get('href'))'''