#!/usr/bin/env python

#
# Usage ./uy.py http://www.patheos.com/blogs/unequallyyoked/2014/01/reading-through-2014-with-pope-francis-index-post.html > text.txt
# Maybe nice to replace all 's -> ""
# Use the output into http://www.tagxedo.com/
# -> Create t-shirts, mug coffee, hoodies, etc.
#
# Don't abuse Patheos bandwidht.
#

# Dependency "Tortoise BeautifulSoup"
from bs4 import BeautifulSoup 
import urllib2, sys

def parsePost (url, includeBlockQuote=False):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup (html)  # Parse HTML
    content = soup.findAll('div',{'class','entry-content'}) # Content
    grafs = content[0].findAll('p') # TODO: Implement quote parse
    txt = ''
    for graf in grafs[1:]:       # Skip Introductory Paragraph about series
        txt = txt + graf.text
    return txt.encode("utf-8")   # Use UTF-8 encoding of text.

def getAllLnks (urlIdx):
    html = urllib2.urlopen(urlIdx).read()
    soup = BeautifulSoup (html)
    content = soup.findAll('div',{'class','entry-content'})
    lnks = content[0].findAll('a')
    links = [lnk['href'] for lnk in lnks]
    return links

def main (url):
    for i in getAllLnks (url):
        if (i.find("www.patheos.com")>0):
            print parsePost(i)
         
if __name__ == "__main__":
    main(sys.argv[1])   
