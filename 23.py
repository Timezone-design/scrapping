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
path = "shop_menu/set/br/"
item_path = "shop_menu/set"
data = []
for i in ['1001-116','1001-117','1005-130','1008-116','1008-143','1010-116','1012-116','1017-130','1017-133','1019-120','1019-134','1025-124','1028-124','1030-117','1031-116','1032-116','1032-119','1032-124','1032-127','1032-138','1032-143','1032-149','1032-151','1032-153','1032-160','1032-169','1034-160','1038-116','1038-130','1038-131','1038-133','1038-173','1039-124','1040-122','1042-116','1042-117','1042-118','1042-120','1042-121','1042-131','1042-132','1042-137','1042-138','1042-141','1042-142','1042-143','1042-153','1045-116','1046-116','1046-118','1050-122','1054-118','1054-119','1059-116','1059-118','1059-120','1059-122','1059-123','1059-124','1059-135','1059-136','1059-137','1059-172','1067-116','1070-140','1077-116','1077-140','1078-116','1078-117','1082-116','1082-120','1086-119','1088-116','1090-116','1090-120','1092-121','1093-133','1093-173','1095-116','1095-117','1097-137','1100-116','1103-130','1103-131','1104-116','1104-117','1104-118','1104-119','1109-122','1109-123','1109-138','1109-141','1109-149','1109-157','1110-134','1110-171','1111-124','1116-125','1116-127','1116-133','1116-160','1116-169','1116-172','1116-173','1122-117','1122-119','1122-122','1122-124','1122-134','1122-155','1135-133','1135-173','1135-174','1136-116','1136-118','1136-119','1138-116','1138-117','1142-138','1144-116','1144-138','1144-150','1144-151','1144-169','1146-130','1146-131','1147-130','1152-119','1156-116','1156-120','1156-121','1156-134','1157-125','1159-116','1159-117','1161-122','1161-123','1161-133','1161-162','1161-172','1161-173','1161-174','1161-175','1161-179','1162-115','1162-116','1162-120','1162-121','1162-122','1162-124','1162-125','1162-126','1162-133','1162-134','1162-135','1162-136','1162-137','1162-153','1162-158','1162-162','1162-171','1162-172','1162-173','1162-175','1162-177','1162-179','1163-116','1164-118','1164-119','1166-135','1167-137','1168-124','1168-132','1169-125','1170-122','1170-123','1170-172','1171-122','1171-123','1171-172','1172-122','1172-123','1173-123','1174-147','1175-143','1176-171','1177-172','1178-172','1179-174','1180-179','1181-116','1181-120','1181-121','1181-134','1181-136','1182-116']:
	page = requests.get(root + path + str(i) + ".html")
	soup = BeautifulSoup(page.content, 'html.parser')

	meta_refresh = getValue(soup.find('meta', attrs = {'http-equiv':'refresh'}), 'content', '0; url=https://www.kts-web.com','')
	meta_title = getValue(soup.find('title'))
	meta_description = getValue(soup.find('meta', attrs = {'name':'description'}), 'content')
	meta_keywords = getValue(soup.find('meta', attrs = {'name':'keywords'}), 'content')

	img = getValue(soup.select('div.brand-info-img img'), 'src', '../..', '/assets/img')
	img_alt = getValue(soup.select('div.brand-info-img img'), 'alt')
	text = getValue(soup.select('div.brand-info-txt a'))
	item_links = soup.select('div.item-banner ul li:first-child a')
	item_images = soup.select('div.item-banner ul li:first-child a img')
	item_texts = soup.select('div.item-banner ul li a')
	items = []
	# print(len(item_links))
	# print(len(item_texts))
	for j in range(len(item_links)):
		item = {
			'link': item_path + getValue(item_links[j], 'href', '..', ''),
			'image': getValue(item_images[j], 'src', '../..', '/assets/img'),
			'image_alt': getValue(item_images[j], 'alt'),
			'text': getValue(item_texts[j*2+1])
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

with open("23.csv", 'w', encoding="UTF-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(row.keys()))
    writer.writeheader()
    for row in data:
    	writer.writerow(row)
