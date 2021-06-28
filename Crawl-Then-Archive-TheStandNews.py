from bs4 import BeautifulSoup
import urllib.request
from archivenow import archivenow

request = urllib.request.Request("https://www.thestandnews.com/politics/")
request.add_header('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')

html_page = urllib.request.urlopen(request)
soup = BeautifulSoup(html_page, features="html.parser")
for link in soup.find_all('a'):
    oglink = str(link.get('href'))
    if oglink.startswith('/politics/'):
        link = "https://www.thestandnews.com"+oglink
        archivenow.push(link,"ia")