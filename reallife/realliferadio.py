#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2

website = "http://www.realliferadio.com/"
page = "http://www.realliferadio.com/fights-in-good-faith-with-leah-libresco.html"

def setup ():
    html = urllib2.urlopen(page).read()
    soup = BeautifulSoup(html)
    mydivs = soup.findAll("div", { "class" : "wsite-html5audio" })
    ll = list()
    for div in mydivs:
        audio = div.find("audio")
        ll.append(website+audio["src"])
    return ll

def save_audio_mp3 (filename, url):
    data = urllib2.urlopen(url)
    size = int(data.headers['content-length'])
    print "Downloading: %s as %s (size %d)"%(url,filename,size)
    downloaded = 0
    CHUNK = 128 * 1024
    with open(filename, 'wb') as fp:
        for chunk in iter(lambda: data.read(CHUNK), ''):
            downloaded += len(chunk)
            print "Downloaded %.2f%%"%(100*downloaded/float(size))
            fp.write (chunk)
    f.close()
    
if __name__ == "__main__":
    audiolist = setup()
    print  "Found %d files"%len(audiolist)
    for i in xrange(len(audiolist)):
        filename = str(i)+".mp3"
        save_audio_mp3 (filename, audiolist[i])
    