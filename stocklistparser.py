from html.parser import HTMLParser
import codecs

class ChinaStockHTMLParser(HTMLParser):
    def __init__(self):
        self.keys = ('name', 'code')
        self.targetclsname = 'result'
        self.divname = ''
        self.parentTag = 'div'
        self.isParentTag = False
        self.targetTag = 'ul'
        self.isTargetTag = False
        self.liTag = 'li'
        self.isLiTag = False
        self.aTag = 'a'
        self.isATag = False
        self.stocks = {}
        self.stock = {}
	def handle_starttag(self, tag, attrs):
		#print("Start tag: ", tag)
        if tag == self.parentTag and attrs['class'] == self.targetclsname :
            self.isParentTag = True
            self.divname = attrs['class']
        if self.isParentTag == True and tag == self.targetTag :
            self.isTargetTag = True
        if self.isTargetTag == True and tag == self.liTag :
            self.isLiTag = True
        if self.isLiTag == True and tag == self.aTag:
            self.isATag = True
            self.stock['website'] = attrs['href'] 
            
	def handle_endtag(self, tag):
        if self.isATag == True and tag == self.aTag:
            self.isATag = False
            self.stock = {}
        if self.isLiTag == True and tag == self.liTag:
            self.isLiTag = False
        if self.isTargetTag == True and tag == self.targetTag :
            self.isLiTag = False
        if self.isParentTag == True and tag == self.parentTage and  self.divname == self.targetclsname :
            self.isTargetTag = False
        
	def handle_data(self, data):
        if self.isATag == True :
            content = data
            self.split_stoke_name_code (content)
            
    def split_stock_name_code(self, stockdata):
        result = stockdata.split('(')
        length = len(result)
        
        for i in range(length):
            key = self.keys[i]
            value = result[i].replace(')','').strip()
            self.stock[key] = value
        
        nstock = {}
        for k,v in self.stock:
            nstock[k] = v
        
        stcode = nstock[self.keys[0]]
        self.stocks[stcode] = nstock

f = codecs.open("stock_agem", encoding="utf-8")
content = f.read()
#print(content)	
parser = ChinaStockHTMLParser()
parser.feed(content)
print(parser.stocks)
