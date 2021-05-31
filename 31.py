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

root = "https://www.kts-web.com/"
path = "product/"
item_path = "shop_menu/set"
data = []
for i in ['body','brake','cooling','drive','engine','intake','interior','other','suspension','ex']:
	page = requests.get(root + path + str(i) + '/index.html')
	soup = BeautifulSoup(page.content, 'html.parser')

	meta_refresh = getValue(soup.find('meta', attrs = {'http-equiv':'refresh'}), 'content', '0; url=https://www.kts-web.com','')
	meta_title = getValue(soup.find('title'))
	meta_description = getValue(soup.find('meta', attrs = {'name':'description'}), 'content')
	meta_keywords = getValue(soup.find('meta', attrs = {'name':'keywords'}), 'content')

	section_titles = soup.select('div.pr_title_2')
	section_item_groups = soup.select('div.pr_title_pc')
	items = []
	if(len(section_titles) == 0 and len(section_item_groups) > 0):
		section_titles = ['']
	for j in range(len(section_titles)):
		try:
			section_item_links = section_item_groups[j].select('a')
			section_item_images = section_item_groups[j].select('a img')
		except:
			section_item_links = soup.select('div.bq_title a')
			section_item_images = soup.select('div.bq_title a img')
		# print(section['title'])
		# print(section_items)
		# break;
		section_items = []
		for k in range(len(section_item_links)):
			item = {
				'link': "/" + path + str(i) + "/" + getValue(section_item_links[k], 'href'),
				'image': '/assets/img/product/' + str(i) + '/' + getValue(section_item_images[k], 'src'),
				'image_alt': getValue(section_item_images[k], 'alt')
			}
			section_items.append(item)

		items.append({
				'title': getValue(section_titles[j]),
				'items': section_items
			})

	row = {
		'url': path + str(i) + "/index.html",
		'meta_refresh': meta_refresh,
		'meta_title': meta_title,
		'meta_description': meta_description,
		'meta_keywords': meta_keywords,
		'items': json.dumps(items, ensure_ascii=False)
	}
	data.append(row)

with open("31.csv", 'w', encoding="UTF-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(row.keys()))
    writer.writeheader()
    for row in data:
    	writer.writerow(row)
