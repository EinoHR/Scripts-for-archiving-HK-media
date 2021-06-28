from bs4 import BeautifulSoup
import urllib.request
from archivenow import archivenow
import multiprocessing as mp

def archivePage(pagenum):
    request = urllib.request.Request(f"https://hongkongfp.com/category/topics/politics-protest/page/{pagenum}/")
    request.add_header('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')

    html_page = urllib.request.urlopen(request)
    soup = BeautifulSoup(html_page, features="html.parser")
    for link in soup.find_all('a'):
        oglink = str(link.get('href'))
        archivenow.push(oglink,"ia")

def main():
    pool = mp.Pool(mp.cpu_count())
    pool.map(archivePage, range(1, 1187))

if __name__ == "__main__":
    main()