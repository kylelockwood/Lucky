#!python

# Opens several google search results

import requests, sys, webbrowser
from bs4 import BeautifulSoup

print('Googling...' + str(sys.argv[1:]))    # Display text while downloading page

# Dupe a browser for google
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

res = requests.get('http://google.com/search?q=' + ' ' .join(sys.argv[1:]),'lxml', headers = headers)
res.raise_for_status()
print('Request status : ' + str(res.status_code))

# Retrieve top search result links
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)

# Open a browser tab for each result
linkElems = soup.select('.r a')

numOpen = min(20, len(linkElems))
# print('numOpen : ' + str(numOpen))
# print('linkElems : ' + str(linkElems))

if numOpen == 0:
    print(f'No results found for {str(sys.argv[1:])}')

for i in range(numOpen):
    # Choose only linkElems that begin with http
    link = str(linkElems[i].get('href'))
    if link.startswith('http'):
        if not 'webcache' in link:
            if not 'walmart' in link:
                print('Link : ' + link)
                webbrowser.open(link)

