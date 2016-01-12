import urllib2
import re
import sys


'''Avoided using beautiful soup and requests and api, I wanted to stick to 
   standard lib as far as possible
'''

TITLE_RE = '<title.*?>(.+?)</title>'
PUBLISHED_RE = '<strong class="watch-time-text">(.+?)</strong>'


pattern = re.compile(TITLE_RE)
pattern2 = re.compile(PUBLISHED_RE)

def get_page(youtube_link):

    try:
        link = urllib2.urlopen(youtube_link)
    except Exception as exc:
        print (exc)

    html = link.read()
    titles=re.findall(pattern,html) 
    publish_date=re.findall(pattern2,html) 
   
    try: 
        t = titles[0]
        pd = publish_date[0]
    except Exception as exc:
        print (exc)
    
    return titles[0], publish_date[0]

if __name__ == "__main__":
    if sys.argv[2] == 'md':
        t, pd = get_page(sys.argv[1])
        print 
        print ("[{}]({})".format(t, sys.argv[1]))
        print ("*{}*".format(pd))


