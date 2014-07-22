#download china stock list
import urllib.request

#http://app.finance.ifeng.com/hq/list.php?type=stock_a&class=ha
baseUrl = http://app.finance.ifeng.com/hq/list.php
types = {'stock_a'}
classes = {'ha','sa', 'gem'}
for type in set(types):
	for cls in set(classes):
		listurl = get_stocklist_url(baseUrl, type, cls)
		html = download_stocklist(listurl)
		print(listurl)
		print(html)
		
download_stocklist(baseUrl
def get_stocklist_url(baseUrl, type, cls):
	return baseUrl + '?type=' + type + '&class=' + cls
	
def download_stocklist(listurl):
	req = urllib.request.Request(listurl)
	response = urllib.request.urlopen(req)
	html = response.read()
	return html
	