#download china stock list
import sys
import urllib.request
import codecs

class ChinaStockDownloader:
	def __init__(self):
		self.baseUrl = 'http://app.finance.ifeng.com/hq/list.php'
		self.types = {'stock_a'}
		self.classes = {'ha','sa', 'gem'}
	
	def get_stocklist_url(self, type, cls):
		return self.baseUrl + '?type=' + type + '&class=' + cls
		
	def download_stocklist(self, listurl):
		req = urllib.request.Request(listurl)
		response = urllib.request.urlopen(req)
		html = response.read()
		return html

	def write_file(self, filename, content):
		#myfile = open(filename, 'w')
		myfile = codecs.open(filename, 'w', 'utf-8')
		myfile.write(str(content))
		myfile.close()
	
	def download_main(self):
		for type in set(self.types):
			for cls in set(self.classes):
				listurl = self.get_stocklist_url(type, cls)
				print("fetch the page: " + listurl)
				html = self.download_stocklist(listurl)
				#codetype = sys.getfilesystemencoding()
				html_code = html.decode('utf-8')
				filename = type+cls
				self.write_file(filename, html_code)
	
#http://app.finance.ifeng.com/hq/list.php?type=stock_a&class=ha
print(sys.getdefaultencoding())
chinastock = ChinaStockDownloader()
chinastock.download_main()
		

	
