from bs4 import BeautifulSoup
import urllib.request
from archivenow import archivenow
import multiprocessing as mp
import time 

def archivePage(pagenum):
    request = urllib.request.Request(f"https://www.inmediahk.net/content_type/column/all?page={pagenum}/")
    request.add_header('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')
    archivenow.push(f"https://www.inmediahk.net/content_type/column/all?page={pagenum}/","ia")

    html_page = urllib.request.urlopen(request)
    soup = BeautifulSoup(html_page, features="html.parser")
    for link in soup.find_all('a'):
        oglink = str(link.get('href'))
        time.sleep(3)
        if oglink.startswith("https://"):
            archivenow.push(oglink,"ia")
        else:
            archivenow.push("https://www.inmediahk.net"+oglink, "ia")

def main():
    pool = mp.Pool(1) #Maximum is 4.
    pool.map(archivePage, range(2796))

if __name__ == "__main__":
    main()