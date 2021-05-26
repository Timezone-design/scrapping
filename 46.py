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
path = "tire_wheel/wheel/"
# item_path = "shop_menu/set"
data = []
for i in ['bbs/fs.html','bbs/fz_mg.html','bbs/lm.html','bbs/lm_r.html','bbs/re_v.html','bbs/rf.html','bbs/rg_f.html','bbs/rg_r.html','bbs/ri_a.html','bbs/ri_d.html','bbs/ri_s.html','bbs/rn.html','bbs/rp.html','bbs/rs_gt.html','bbs/rs_n.html','bbs/rz_d.html','bbs/super_rs.html','doall/fenice_tt1.html','enkei/performanceline_pf01.html','enkei/performanceline_pf01evo.html','enkei/performanceline_pf01ss.html','enkei/performanceline_pf07.html','g_corporation/moving_cafe_label_open_heart2.html','g_corporation/moving_cafe_label_swing_heart.html','piaa/dw_jh.html','r_pride/wado_sakura.html','r_pride/wado_sakura_5buzaki.html','rays/gramlights_57fxx.html','rays/gramlights_57jv.html','rays/gramlights_57xtreme_sp_spec.html','rays/gramlights_57xtreme_std_spec.html','rays/versus_stratagia_vouge.html','rays/volk_c28n_10.html','rays/volk_c28n_8.html','rays/volk_ce28_cr.html','rays/volk_g25.html','rays/volk_te37.html','rays/volk_te37_g.html','rays/volk_te37_kcr.html','rays/volk_te37_kcr_bz.html','rays/volk_te37_sl.html','rays/volk_te37_ultra.html','rays/volk_te37_v.html','rays/volk_ze40.html','ssr/executor_cv01s.html','ssr/executor_cv02s.html','ssr/executor_cv03s.html','ssr/executor_ex01.html','ssr/executor_ex02.html','ssr/executor_ex03.html','ssr/executor_ex04.html','ssr/gt_f01.html','ssr/gt_v01.html','ssr/gt_v02.html','ssr/gt_v03.html','ssr/professor_ms1.html','ssr/professor_ms1r.html','ssr/professor_ms3.html','ssr/professor_ms3r.html','ssr/professor_sp1.html','ssr/professor_sp1r.html','ssr/professor_sp4.html','ssr/professor_sp4r.html','ssr/speed_star_fl2.html','ssr/speed_star_mk1.html','ssr/speed_star_mk2.html','ssr/speed_star_mk3.html','weds/kranze_acuerdo.html','weds/kranze_verae.html','weds/kranze_verae_16_17.html','weds/kranze_verae_713_evo.html','weds/kranze_verae_713_evo_16_17.html','weds/leonis_vx.html','weds/leonis_wx.html','weds/maverick_605s.html','weds/wedssport_sa_10r.html','weds/wedssport_sa_72r.html','work/emotion_11r.html','work/emotion_cr_2p.html','work/emotion_cr_kiwami.html','work/emotion_d9r.html','work/emotion_t7r_2p.html','work/meister_cr01.html','work/meister_m1.html','work/meister_s1_2p.html','work/meister_s1_3p.html','work/meister_s1r.html','work/schwert_sc4.html','yokohama/advan_gt.html','yokohama/advan_gt_18.html','yokohama/advan_gt_pv.html','yokohama/advan_rc3.html','yokohama/advan_rg3.html','yokohama/advan_rs_d.html','yokohama/advan_rs_df.html','yokohama/advan_rs2.html','yokohama/advan_rt.html','yokohama/advan_rz.html','yokohama/avs_model_f15.html','yokohama/avs_model_f50.html','bbs/re_l2.html']:
	page = requests.get(root + path + str(i))
	soup = BeautifulSoup(page.content, 'html.parser')

	meta_refresh = getValue(soup.find('meta', attrs = {'http-equiv':'refresh'}), 'content', '0; url=https://www.kts-web.com','')
	meta_title = getValue(soup.find('title'))
	meta_description = getValue(soup.find('meta', attrs = {'name':'description'}), 'content')
	meta_keywords = getValue(soup.find('meta', attrs = {'name':'keywords'}), 'content')
	try:
		logo = getValue(soup.select('div.th_title_730 img')[1], 'src', 'img/', '/assets/img/tire_wheel/wheel/img/')
		logo_alt = getValue(soup.select('div.th_title_730 img')[1], 'alt')
	except:
		try:
			logo = getValue(soup.select('div.th_title_730 img')[0], 'src', 'img/', '/assets/img/tire_wheel/wheel/img/')
			logo_alt = getValue(soup.select('div.th_title_730 img')[0], 'alt')
		except:
			print(i)
	# img = getValue(soup.select('img.th_tire_img'), 'src', 'img/', '/assets/img/tire_wheel/wheel/img/')
	# img_alt = getValue(soup.select('img.th_tire_img'), 'alt')
	prod_name = getValue(soup.select('div.th_comm_bar_3px'))
	pdf = path + i.split('/')[0] + '/' + getValue(soup.select('div.th_tire_price a'), 'href')
	text = getValue(soup.select('div.th_table_cell'))
	# item_links = soup.select('div.th_maker_top_list_cell2 a.link_n')
	images = soup.select('div.mod_bbs_photo_entry img')
	items = []
	for j in range(len(images)):
		item = {
			'image': path + i.split('/')[0] + '/' + getValue(images[j], 'src'),
			'image_alt': getValue(images[j], 'alt'),
		}
		items.append(item)
	row = {
		'url': path + str(i),
		'meta_refresh': meta_refresh,
		'meta_title': meta_title,
		'meta_description': meta_description,
		'meta_keywords': meta_keywords,
		'prod_name': prod_name,
		'pdf': pdf,
		'text': text,
		'logo': logo,
		'logo_alt': logo_alt,
		'items': json.dumps(items, ensure_ascii=False)
	}
	data.append(row)

with open("43.csv", 'w', encoding="UTF-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(row.keys()))
    writer.writeheader()
    for row in data:
    	writer.writerow(row)
