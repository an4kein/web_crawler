import requests
import re

to_crawl = ['http://g1.globo.com']

crawled = set()

req = requests.get(to_crawl[0])

html = req.text



#padrao = re.search(r'href=[\'"][\w:/\.]+', html)
padrao = re.findall(r'href=[\'"][\w:/\.]+', html)


#print padrao.group()
for link in padrao:
    print link
