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
			
			try:

				proxy['ip'] = items.select("td")[0].text
				proxy['port'] = items.select("td")[1].text
				proxy['country_code'] = items.select("td")[2].text
				proxy['country'] = 'United States'
				proxy['anonymity'] = items.select("td")[4].text
				proxy['google'] = items.select("td")[5].text
				proxy['https'] = items.select("td")[6].text
				proxy['last_checked'] = items.select("td")[7].text

			except:

				pass

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

			try:
				
				proxy['ip'] = items.select("td")[0].text
				proxy['port'] = items.select("td")[1].text
				proxy['country_code'] = items.select("td")[2].text
				proxy['country'] = items.select("td")[3].text
				proxy['anonymity'] = items.select("td")[4].text
				proxy['google'] = items.select("td")[5].text
				proxy['https'] = items.select("td")[6].text
				proxy['last_checked'] = items.select("td")[7].text

			except:

				pass

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
