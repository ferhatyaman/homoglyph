import json
from urllib.parse import urlparse
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.data = ''
	def handle_data(self, data):
		self.data = data

			

class TwitterData:
	"""docstring for TwitterData"""
	def __init__(self):
		super(TwitterData, self).__init__()

	def readDomains(self,line):
		parser = MyHTMLParser()
		if line != "\n":
			line_object = json.loads(line)
			htmltag = line_object['source']
			parser.feed(htmltag)
			return parser.data
		