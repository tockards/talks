import urllib2
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):


def get_page(youtube_link):

    try:
        link = urllib2.urlopen(youtube_link)
    except Exception as exc:
        print (exc)

    html = link.read()

    return html


