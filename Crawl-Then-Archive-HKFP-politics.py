from bs4 import BeautifulSoup
import urllib.request
from archivenow import archivenow
import multiprocessing as mp
import time 

def archivePage(pagenum):
    request = urllib.request.Request(f"https://hongkongfp.com/category/topics/politics-protest/page/{pagenum}/")
    request.add_header('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')
    archivenow.push(f"https://hongkongfp.com/category/topics/politics-protest/page/{pagenum}/","ia")

    html_page = urllib.request.urlopen(request)
    soup = BeautifulSoup(html_page, features="html.parser")
    for article in soup.find_all('article'):
        time.sleep(1.5)
        for link in article.find_all('a'):
            oglink = str(link.get('href'))
            time.sleep(0.5)
            archivenow.push(oglink,"ia")

def main():
    pool = mp.Pool(3) #Maximum is 4.
    pool.map(archivePage, range(1, 1188))

if __name__ == "__main__":
    main()