import requests
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import csv
import json

data = []
for i in [100,101,102,103,104,105,106,107,108,109,110,111,112,113,115]:
	page = requests.get("http://localhost/shop_menu/set/cat/"+str(i)+".html")
	soup = BeautifulSoup(page.content, 'html.parser')
	try:
		img = soup.select('div.cat-info-img img')[0]['src']
	except:
		print(i)
		continue

	text = soup.select('div.cat-info-txt a')[0].get_text()
	cat_baner_links = soup.select('div.cat-banner_s li a')
	cat_baner_images = soup.select('div.cat-banner_s li a img')

	row = {
		'url': "shop_menu/set/cat/"+str(i)+".html",
		'img': img.replace('../..', '/assets/img'),
		'text': text
	}
	data.append(row)

with open("data.csv", 'w', encoding="UTF-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(row.keys()))
    writer.writeheader()
    for datum in data:
    	writer.writerow({'url': datum['url'], 'img': datum['img'], 'text':datum['text']})

