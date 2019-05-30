#!/usr/bin/python
__author__ = "Justin Stals"

import requests
import re
from bs4 import BeautifulSoup

hdr = { 'Accept': 'text/html,application/xhtml+xml,*/*',"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}

def get_proxies(usa=True, international=True):

	proxies = {}

	if usa:
		res = requests.get('https://www.us-proxy.org/', headers=hdr)
		soup = BeautifulSoup(res.text, "html.parser")

		for items in soup.select("tbody tr"):
			proxy = {}
			i = 0
			for item in items.select("td"):
				if i == 0:
					proxy['ip'] = item.text
				elif i == 1:
					proxy['port'] = item.text
				elif i == 2:
					proxy['country_code'] = item.text
				elif i == 3:
					proxy['country'] = 'United States'
				elif i == 4:
					proxy['anonymity'] = item.text
				elif i == 5:
					proxy['google'] = item.text
				elif i == 6:
					proxy['https'] = item.text
				elif i == 7:
					proxy['last_checked'] = item.text
				i+=1

			if proxy['anonymity'] == 'elite proxy' and proxy['https'] == 'yes':
				if proxy['country'] in proxies:
					proxies[proxy['country']].append(proxy)
				else:
					proxies[proxy['country']] = [proxy]

		print('US proxies pulled in from us-proxy.org')

	if international:
		res = requests.get('https://free-proxy-list.net/', headers=hdr)
		soup = BeautifulSoup(res.text, "html.parser")

		for items in soup.select("tbody tr"):
			proxy = {}
			i = 0
			for item in items.select("td"):
				if i == 0:
					proxy['ip'] = item.text
				elif i == 1:
					proxy['port'] = item.text
				elif i == 2:
					proxy['country_code'] = item.text
				elif i == 3:
					proxy['country'] = item.text
				elif i == 4:
					proxy['anonymity'] = item.text
				elif i == 5:
					proxy['google'] = item.text
				elif i == 6:
					proxy['https'] = item.text
				elif i == 7:
					proxy['last_checked'] = item.text
				i+=1

			if proxy['anonymity'] == 'elite proxy' and proxy['https'] == 'yes':
				if proxy['country'] in proxies:
					proxies[proxy['country']].append(proxy)
				else:
					proxies[proxy['country']] = [proxy]

		print('International proxies pulled in from free-proxy-list.net')


	print('Proxies available:')
	
	for k, v in proxies.items():
		print(k, len(v))

	return proxies

if __name__ == "__main__":
	get_proxies(True, True)
