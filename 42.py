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
path = "tire_wheel/tire/"
item_path = "shop_menu/set"
data = []
for i in ['bridgestone','dunlop','falken','federal','goodyear','kenda','michelin','nankang','toyo_tires','yokohama']:
	page = requests.get(root + path + str(i) + "/index.html")
	soup = BeautifulSoup(page.content, 'html.parser')

	meta_refresh = getValue(soup.find('meta', attrs = {'http-equiv':'refresh'}), 'content', '0; url=https://www.kts-web.com','')
	meta_title = getValue(soup.find('title'))
	meta_description = getValue(soup.find('meta', attrs = {'name':'description'}), 'content')
	meta_keywords = getValue(soup.find('meta', attrs = {'name':'keywords'}), 'content')

	img = getValue(soup.select('img.sp_img_100p'), 'src', 'img/', '/assets/img/tire_wheel/tire/img/')
	img_alt = getValue(soup.select('img.sp_img_100p'), 'alt')
	text = ''
	item_links = soup.select('div.th_maker_top_list_cell2 a.link_n')
	item_images = soup.select('div.th_maker_top_list_cell2 img')
	items = []
	for j in range(len(item_links)):
		item = {
			'link': path + str(i) + "/" + getValue(item_links[j], 'href'),
			'image': getValue(item_images[j], 'src', 'img/', '/assets/img/tire_wheel/tire/img/'),
			'image_alt': getValue(item_images[j], 'alt'),
			'text': getValue(item_links[j])
		}
		items.append(item)
	row = {
		'url': path + str(i) + "/index.html",
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

with open("42.csv", 'w', encoding="UTF-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(row.keys()))
    writer.writeheader()
    for row in data:
    	writer.writerow(row)
