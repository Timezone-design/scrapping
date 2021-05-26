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
path = "shop_menu/set/item/"
item_path = "shop_menu/set"
data = []
for i in [10000,10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10017,10018,10019,10020,10021,10022,10023,10024,10025,10026,10027,10028,10029,10030,10031,10032,10033,10034,10035,10036,10037,10038,10039,10040,10041,10042,10043,10044,10045,10046,10047,10048,10049,10050,10051,10052,10053,10054,10055,10056,10057,10058,10059,10060,10061,10062,10063,10064,10065,10066,10067,10068,10069,10070,10071,10072,10075,10076,10077,10079,10080,10081,10082,10083,10084,10085,10088,10089,10090,10091,10092,10094,10095,10096,10097,10098,10099,10100,10101,10102,10103,10104,10105,10106,10107,10108,10109,10110,10111,10112,10115,10116,10117,10118,10119,10121,10122,10123,10125,10126,10127,10128,10130,10131,10132,10133,10134,10135,10136,10137,10138,10139,10140,10141,10142,10144,10145,10146,10147,10148,10149,10150,10151,10153,10154,10155,10156,10158,10159,10160,10161,10162,10163,10164,10165,10166,10167,10168,10169,10170,10171,10172,10173,10175,10176,10177,10178,10181,10182,10183,10184,10185,10186,10187,10188,10189,10190,10191,10192,10195,10196,10197,10198,10199,10200,10201,10202,10213,10214,10215,10216,10217,10218,10219,10220,10221,10222,10223,10224,10226,10227,10228,10229,10230,10231,10232,10233,10234,10235,10237,10238,10239,10240,10241,10242,10243,10244,10245,10246,10248,10249,10250,10251,10252,10253,10270,10271,10272,10275,10292,10293,10294,10295,10296,10297,10298,10299,10300,10301,10302,10303,10304,10305,10306,10344,10345,10346,10347,10350,10351,10353,10354,10355,10356,10359,10360,10361,10367,10368,10369,10370,10371,10372,10430,10435,10436,10437,10439,10446,10447,10450,10453,10455,10456,10457,10458,10462,10463,10464,10467,10469,10472,10474,10477,10479,10483,10484,10500,10524,10525,10526,10527,10528,10529,10531,10534,10535,10536,10538,10539,10540,10541,10542,10543,10553,10554,10555,10556,10557,10558,10559,10560,10561,10562,10563,10564,10565,10566,10567,10568,10569,10570,10571,10610,10621,10625,10628,10629,10667,10668,10669,10670,10671,10672,10673,10675,10676,10677,10678,10679,10680,10681,10682,10683,10684,10685,10686,10687,10688,10689,10690,10691,10692,10695,10696,10697,10698,10699,10700,10701,10703,10704,10706,10708,10709,10710,10712,10713,10714,10715,10716,10717,10719,10722,10723,10725,10726,10727,10729,10730,10731,10732,10733,10736,10737,10741,10744,10745,10746,10747,10748,10749,10750,10751,10752,10754,10755,10756,10757,10758,10759,10760,10762,10764,10765,10766,10767,10768,10770,10771,10773,10774,10775,10776,10777,10778,10781,10784,10787,10788,10789,10790,10791,10793,10795,10796,10800,10802,10803,10247,10339,10340,10341,10342,10804,10805,10806,10807,10808,10809,10810,10811,10812,10813,10814,10815,10816,10817,10818,10819,10820,10613,10487,10499,10454,10488,10489,10490,10491,10492,10493,10494,10495,10502,10612,10611,10486,10544,10501,10289,10255,10631,10630,10284,10285,10287,10288,10290,10616,10617,10618,10619,10620,10626,10638,10632,10633,10634,10614,10273,10822,10311,10313,10314,10315,10316,10317,10319,10320,10321,10322,10323,10324,10325,10330,10332,10333,10334,10335,10337,10338]:
	page = requests.get(root + path + str(i) + ".php")
	soup = BeautifulSoup(page.content, 'html.parser')

	meta_refresh = getValue(soup.find('meta', attrs = {'http-equiv':'refresh'}), 'content', '0; url=https://www.kts-web.com','')
	meta_title = getValue(soup.find('title'))
	meta_description = getValue(soup.find('meta', attrs = {'name':'description'}), 'content')
	meta_keywords = getValue(soup.find('meta', attrs = {'name':'keywords'}), 'content')

	logo = getValue(soup.select('div.set_menu_n_330 img'), 'src', '../..', '/assets/img')
	logo_alt = getValue(soup.select('div.set_menu_n_330 img'), 'alt')
	img1 = getValue(soup.select('div.swiper-slide-active img'), 'src', '../..', '/assets/img')
	img1_alt = getValue(soup.select('div.swiper-slide-active img'), 'alt')
	img2 = getValue(soup.select('div.swiper-slide-next img'), 'src', '../..', '/assets/img')
	img2_alt = getValue(soup.select('div.swiper-slide-next img'), 'alt')
	img3 = getValue(soup.select('div.swiper-slide-prev img'), 'src', '../..', '/assets/img')
	img3_alt = getValue(soup.select('div.swiper-slide-prev img'), 'alt')
	change_link = getValue(soup.select('a.change_button'), 'href', '../..', '/shop_menu')
	brand_name = getValue(soup.select('div.item_info_text_middle p'))
	prod_name = getValue(soup.select('div.item_info_text_middle_b p'))
	text1 = getValue(soup.select('div#panel1 p'))
	text2 = getValue(soup.select('div#panel2 p'))
	
	row = {
		'url': path + str(i) + ".php",
		'meta_refresh': meta_refresh,
		'meta_title': meta_title,
		'meta_description': meta_description,
		'meta_keywords': meta_keywords,
		'logo': logo,
		'logo_alt': logo_alt,
		'img1': img1,
		'img2': img2,
		'img3': img3,
		'img1_alt': img1_alt,
		'img2_alt': img2_alt,
		'img3_alt': img3_alt,
		'change_link': change_link,
		'brand_name': brand_name,
		'prod_name': prod_name,
		'text1': text1,
		'text2': text2,
	}
	data.append(row)

with open("24.csv", 'w', encoding="UTF-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(row.keys()))
    writer.writeheader()
    for row in data:
    	writer.writerow(row)
