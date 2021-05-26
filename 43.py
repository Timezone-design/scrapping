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
path = "tire_wheel/tire/"
item_path = "shop_menu/set"
data = []
for i in ['bridgestone/blizzak.html','bridgestone/ecopia.html','bridgestone/nextry.html','bridgestone/playz.html','bridgestone/potenza.html','bridgestone/regno.html','dunlop/as.html','dunlop/comfort.html','dunlop/eco.html','dunlop/import.html','dunlop/mos.html','dunlop/sport.html','dunlop/suv.html','dunlop/winter.html','falken/azenis.html','falken/dress_up_van.html','falken/espia.html','falken/eurowinter.html','falken/sincera.html','falken/wildpeak.html','falken/ziex.html','federal/comfort.html','federal/luxury_sports.html','federal/specialty.html','federal/sports.html','goodyear/all.html','goodyear/comfort.html','goodyear/sport.html','goodyear/studless.html','goodyear/suv.html','goodyear/van.html','kenda/minivan.html','kenda/sport.html','kenda/std.html','kenda/suv.html','michelin/crossclimate.html','michelin/energy.html','michelin/latitude.html','michelin/pilot.html','michelin/premier.html','michelin/primacy.html','nankang/econex.html','nankang/nk_comfort.html','nankang/racing.html','nankang/rollnex.html','nankang/sportnex.html','toyo_tires/all_season.html','toyo_tires/nanoenergy.html','toyo_tires/open_country.html','toyo_tires/proxes.html','toyo_tires/sd_7.html','toyo_tires/studless.html','toyo_tires/tranpath.html','yokohama/advan.html','yokohama/bluearth.html','yokohama/ecos.html','yokohama/geolandar.html','yokohama/ice_guard.html','yokohama/parada.html']:
	page = requests.get(root + path + str(i))
	soup = BeautifulSoup(page.content, 'html.parser')

	meta_refresh = getValue(soup.find('meta', attrs = {'http-equiv':'refresh'}), 'content', '0; url=https://www.kts-web.com','')
	meta_title = getValue(soup.find('title'))
	meta_description = getValue(soup.find('meta', attrs = {'name':'description'}), 'content')
	meta_keywords = getValue(soup.find('meta', attrs = {'name':'keywords'}), 'content')
	try:
		logo = getValue(soup.select('div.th_title_730 img')[1], 'src', 'img/', '/assets/img/tire_wheel/tire/img/')
		logo_alt = getValue(soup.select('div.th_title_730 img')[1], 'alt')
	except:
		try:
			logo = getValue(soup.select('div.th_title_730 img')[0], 'src', 'img/', '/assets/img/tire_wheel/tire/img/')
			logo_alt = getValue(soup.select('div.th_title_730 img')[0], 'alt')
		except:
			print(i)
	img = getValue(soup.select('img.th_tire_img'), 'src', 'img/', '/assets/img/tire_wheel/tire/img/')
	img_alt = getValue(soup.select('img.th_tire_img'), 'alt')
	# text = ''
	# item_links = soup.select('div.th_maker_top_list_cell2 a.link_n')
	# item_images = soup.select('div.th_maker_top_list_cell2 img')
	# items = []
	# for j in range(len(item_links)):
	# 	item = {
	# 		'link': path + str(i) + "/" + getValue(item_links[j], 'href'),
	# 		'image': getValue(item_images[j], 'src', 'img/', '/assets/img/tire_wheel/tire/img/'),
	# 		'image_alt': getValue(item_images[j], 'alt'),
	# 		'text': getValue(item_links[j])
	# 	}
	# 	items.append(item)
	row = {
		'url': path + str(i),
		'meta_refresh': meta_refresh,
		'meta_title': meta_title,
		'meta_description': meta_description,
		'meta_keywords': meta_keywords,
		'img': img,
		'img_alt': img_alt,
		'logo': logo,
		'logo_alt': logo_alt
	}
	data.append(row)

with open("43.csv", 'w', encoding="UTF-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(row.keys()))
    writer.writeheader()
    for row in data:
    	writer.writerow(row)
