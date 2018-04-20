import requests
import re

to_crawl = ['http://g1.globo.com']

crawled = set()

req = requests.get(to_crawl[0])

html = req.text



padrao = re.search(r'href="\w+://\w+.\w+.\w+"', html)


print padrao.group()
