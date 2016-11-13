import urllib
import urllib2
import re

baseurl = 'http://www.offershow.online:8000'
tail = "/offersearch/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(baseurl + tail, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<li>.*?<a href="(.*?)" data-ajax= "false" >(.*?)<span class="ui-li-count">(.*?)</span>.*?</a>.*?</li>',re.S)
    items = re.findall(pattern,content)
    i = 0
    for item in items:
        if i > 10:
            break
        i+=1
        detail_request = urllib2.Request(baseurl + item[0])
        detail_response = urllib2.urlopen(detail_request)
        details = detail_response.read().decode('utf-8')
        # print details
        pattern2 = re.compile('<div class="ui-block-[ab]"><p align="center".*?>(.*?)</p></div>')
        detail_items = re.findall(pattern2, details)
        print '--------------------------'
        for detail_item in detail_items:
            print detail_item
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason  
