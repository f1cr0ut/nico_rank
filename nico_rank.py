#!/usr/bin/python
#python3.5
import io
import sys
import urllib
import urllib.request
import urllib.parse
import http
import http.cookiejar
import xml.etree.ElementTree as etree

class crowler:
	def __init__(self):
		self.connect = 0
		self.response = ''
		self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

	def visit(self, url, post_data = None):
		if post_data == None:
			self.connect = self.opener.open(url)
		else:
			data = urllib.parse.urlencode(post_data).encode('utf-8')
			self.connect = self.opener.open(url, data)
		self.response = self.connect.read().decode('utf-8')

if __name__ == '__main__':
	crowl = crowler()
	crowl.visit('http://www.nicovideo.jp/ranking/fav/hourly/all?rss=2.0')
	tree = etree.fromstring(crowl.response)
	length = 0
	end = 100
	if len(sys.argv) > 1:
		end = int(sys.argv[1])
	for i in tree.findall('.//item'):
		print(i.find('.//title').text)
		print(i.find('.//link').text + '\n')
		length += 1
		if length >= end:
			break
