from html.parser import HTMLParser
import codecs

class ChinaStockHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print("Start tag: ", tag)
	def handle_endtag(self, tag):
		print("End tag: ", tag)
	def handle_data(self, data):
		print("Some data: ", data)

f = codecs.open("stock_agem", encoding="utf-8")
content = f.read()
#print(content)	
parser = ChinaStockHTMLParser()
parser.feed(content)