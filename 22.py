import requests
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import csv
import json

def getValue(element, attribute = '', str1 = '', str2 = ''):
	element = (element[0] if len(element) > 0 else False) if isinstance(element, list) else element
	try:
		return (element.get_text().replace(str1, str2) if attribute == '' else element[attribute].replace(str1, str2)) if element else ''
	except:
		return ''

root = "http://localhost/"
path = "shop_menu/set/cat/"
item_path = "shop_menu/set"
data = []
for i in [116,117,118,119,120,121,122,123,124,125,126,127,130,131,132,133,134,135,136,137,138,140,141,142,143,147,149,150,151,153,155,157,158,160,162,169,171,172,173,174,175,177,179]:
	page = requests.get(root + path + str(i) + ".html")
	soup = BeautifulSoup(page.content, 'html.parser')

	meta_refresh = getValue(soup.find('meta', attrs = {'http-equiv':'refresh'}), 'content', '0; url=https://www.kts-web.com','')
	meta_title = getValue(soup.find('title'))
	meta_description = getValue(soup.find('meta', attrs = {'name':'description'}), 'content')
	meta_keywords = getValue(soup.find('meta', attrs = {'name':'keywords'}), 'content')

	img = getValue(soup.select('div.cat-info-img img'), 'src', '../..', '/assets/img')
	img_alt = getValue(soup.select('div.cat-info-img img'), 'alt')
	text = getValue(soup.select('div.cat-info-txt a'))
	item_links = soup.select('ul.brand-banner li a')
	item_images = soup.select('ul.brand-banner li a img')
	items = []
	for j in range(len(item_links)):
		item = {
			'link': item_path + getValue(item_links[j], 'href', '..', ''),
			'image': getValue(item_images[j], 'src', '../..', '/assets/img'),
			'image_alt': getValue(item_images[j], 'alt'),
			'text': getValue(item_links[j])
		}
		items.append(item)
	row = {
		'url': path + str(i) + ".html",
		'meta_refresh': meta_refresh,
		'meta_title': meta_title,
		'meta_description': meta_description,
		'meta_keywords': meta_keywords,
		'img': img,
		'img_alt': img_alt,
		'text': text,
		'items': json.dumps(items, ensure_ascii=False)
	}
	data.append(row)

with open("22.csv", 'w', encoding="UTF-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(row.keys()))
    writer.writeheader()
    for row in data:
    	writer.writerow(row)
