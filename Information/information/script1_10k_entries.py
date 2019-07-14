city_province_pairs = [
("Beijing", "Beijing"), 

("Dongguan", "Guangdong"), ("Guangzhou", "Guangdong"), ("Zhongshan", "Guangdong"), ("Shenzhen", "Guangdong"), ("Huizhou", "Guangdong"), 
("Jiangmen", "Guangdong"), ("Zhuhai", "Guangdong"), ("Shantou", "Guangdong"), ("Foshan", "Guangdong"), ("Qianjiang", "Guangdong"),

("Jinan", "Shandong"), ("Qingdao", "Shandong"), ("Linyi", "Shandong"), ("Jining", "Shandong"), ("Heze", "Shandong"), 
("Yantai", "Shandong"), ("Yantai", "Shandong"), ("Huaifang", "Shandong"), ("Rizhao", "Shandong"), ("Weihai", "Shandong"),

("Suzhou", "Jiangsu"), ("Xuzhou", "Jiangsu"), ("Yancheng", "Jiangsu"), ("Wuxi", "Jiangsu"), ("Nanjing", "Jiangsu"), 
("Nantong", "Jiangsu"), ("Lianyungang", "Jiangsu"), ("Changzhou", "Jiangsu"), ("Zhenjiang", "Jiangsu"), ("Yangzhou", "Jiangsu"),

("Zhengzhou", "Henan"), ("Nanyang", "Henan"), ("Xinxiang", "Henan"), ("Anyang", "Henan"), ("Luoyang", "Henan"),
("Xinyang", "Henan"), ("Pingdingshan", "Henan"), ("Zhoukou", "Henan"), ("Shangqiu", "Henan"), ("Kaifeng", "Henan"),

("Shanghai", "Shanghai"),

("Shijiazhuang", "Hebei"), ("Tangshan", "Hebei"), ("Baoding", "Hebei"), ("Handan", "Hebei"), ("Cangzhou", "Hebei"),
("Qinhuangdao", "Hebei"), ("Zhangjiakou", "Hebei"), ("Hengshui", "Hebei"), ("Langfang", "Hebei"), ("Chengde", "Hebei"),

("Wenzhou", "Zhejiang"), ("Ningbo", "Zhejiang"), ("Hangzhou", "Zhejiang"), ("Taizhou", "Zhejiang"), ("Jiaxing", "Zhejiang"), 
("Jinhua", "Zhejiang"), ("Huzhou", "Zhejiang"), ("Shaoxing", "Zhejiang"), ("Zhoushan", "Zhejiang"), ("Lishui", "Zhejiang"),

("Xianggang", "Xianggang"),

("Xian", "Shanxi"), ("Xianyang", "Shanxi"), ("Baoji", "Shanxi"), ("Baoji", "Shanxi"), ("Hanzhong", "Shanxi"),
("Weinan", "Shanxi"), ("Ankang", "Shanxi"), ("Yulin", "Shanxi"), ("Shangluo", "Shanxi"), ("Yanan", "Shanxi"),

("Changsha", "Hunan"), ("Shaoyang", "Hunan"), ("Changde", "Hunan"), ("Hengyang", "Hunan"), ("Zhuzhou", "Hunan"),
("Xiangtan", "Hunan"), ("Yongzhou", "Hunan"), ("Yueyang", "Hunan"), ("Huaihua", "Hunan"), ("Yiyang", "Hunan"),

("Chongqing", "Chongqing"),

("Zhangzhou", "Fujian"), ("Xiamen", "Fujian"), ("Quanzhou", "Fujian"), ("Fuzhou", "Fujian"), ("Putian", "Fujian"),
("Ningde", "Fujian"), ("Sanming", "Fujian"), ("Nanping", "Fujian"), ("Longyan", "Fujian"),

("Tianjin", "Tianjin"),

("Nanming", "Yunnan"), ("Honghe", "Yunnan"), ("Dali", "Yunnan"), ("Wenshan", "Yunnan"), ("Dehong", "Yunnan"),
("Qujing", "Yunnan"), ("Shaotong", "Yunnan"), ("Chuxiong", "Yunnan"), ("Baoshan", "Yunnan"), ("Yuxi", "Yunnan"),

("Chengdu", "Sichuan"), ("Mianyang", "Sichuan"), ("Guangyuan", "Sichuan"), ("Dazhou", "Sichuan"), ("Nanchong", "Sichuan"),
("Deyang", "Sichuan"), ("Guangan", "Sichuan"), ("Aba", "Sichuan"), ("Bazhong", "Sichuan"), ("Suining", "Sichuan"),

("Guigang", "Guangxi"), ("Yulin", "Guangxi"), ("Beihai", "Guangxi"), ("Nanning", "Guangxi"), ("Liuzhou", "Guangxi"),
("Guilin", "Guangxi"), ("Wuzhou", "Guangxi"), ("Qinzhou", "Guangxi"), ("Laibing", "Guangxi"), ("Hechi", "Guangxi"),

("Wuhu", "Anhui"), ("Hefei", "Anhui"), ("Liuan", "Anhui"), ("Suzhou", "Anhui"), ("Anqing", "Anhui"),
("Maanshan", "Anhui"), ("Huaibei", "Anhui"), ("Huainan", "Anhui"), ("Yicheng", "Anhui"), ("Huangshan", "Anhui"),

("Sanya", "Hainan"), ("Haikou", "Hainan"), ("Qionghai", "Hainan"), ("Wenchang", "Hainan"), ("Dongwan", "Hainan"),
("Wuzhishan", "Hainan"), ("Wanning", "Hainan"), ("Lingao", "Hainan"), ("Baisha", "Dingnan"), ("Qiongzhong", "Hainan"),

("Nanchang", "Jiangxi"), ("Ganzhou", "Jiangxi"), ("Shangrao", "Jiangxi"), ("Jian", "Jiangxi"), ("Jiujiang", "Jiangxi"),
("Xinyu", "Jiangxi"), ("Fuzhou", "Jiangxi"), ("Jingdezhen", "Jiangxi"), ("Pingxiang", "Jiangxi"), ("Yingtan", "Jiangxi"),

("Wuhan", "Hubei"), ("Xiantao", "Hubei"), ("Xiangfan", "Hubei"), ("Jingzhou", "Hubei"), ("Enshi", "Hubei"),
("Huanggang", "Hubei"), ("Xiaogan", "Hubei"), ("Shiyan", "Hubei"), ("Huangshi", "Hubei"), ("Tianmen", "Hubei"),

("Taiyuan", "Shanxi"), ("Datong", "Shanxi"), ("Yuncheng", "Shanxi"), ("Changzhi", "Shanxi"), ("Jincheng", "Shanxi"),
("Linfen", "Shanxi"), ("Luliang", "Shanxi"), ("Jinzhong", "Shanxi"), ("Yangquan", "Shanxi"), ("Shuozhou", "Shanxi"),

("Dalian", "Liaoning"), ("Shenyang", "Liaoning"), ("Dandong", "Liaoning"), ("Liaoyang", "Liaoning"), ("Huludao", "Liaoning"),
("Jinzhou", "Liaoning"), ("Yingkou", "Liaoning"), ("Anshan", "Liaoning"), ("Fushun", "Liaoning"), ("Panjin", "Liaoning"),

("Taibei", "Taiwan"), ("Gaoxiong", "Taiwan"), ("Taizhong", "Taiwan"), ("Xinzhu", "Taiwan"), ("Jilong", "Taiwan"),
("Jilong", "Tainan"), ("Jiayi", "Taiwan"),

("Qiqihaer", "Heilongjiang"), ("Haerbing", "Heilongjiang"), ("Daqing", "Heilongjiang"), ("Jiamusi", "Heilongjiang"), ("Shuangyashan", "Heilongjiang"),
("Mudanjiang", "Heilongjiang"), ("Jixi", "Heilongjiang"), ("Heihe", "Heilongjiang"), ("Suihua", "Heilongjiang"), ("Hegang", "Heilongjiang"),

("Chifeng", "Neimenggu"), ("Baotou", "Neimenggu"), ("Tongliao", "Neimenggu"), ("Huhehaote", "Neimenggu"), ("Eerduosi", "Neimenggu"),
("Wuhai", "Neimenggu"), ("Hulunbeier", "Neimenggu"), ("Xingan", "Neimenggu"), ("Wulanchabu", "Neimenggu"), ("Xilinguole", "Neimenggu"),

("Aomen", "Aomen"),

("Guiyang", "Guizhou"), ("Qiandongnan", "Guizhou"), ("Qiannan", "Guizhou"), ("Zunyi", "Guizhou"), ("Qianxinan", "Guizhou"),
("Bijie", "Guizhou"), ("Tongren", "Guizhou"), ("Anshun", "Guizhou"), ("Liupanshui", "Guizhou"),

("Lanzhou", "Gansu"), ("Tianshui", "Gansu"), ("Qingyang", "Gansu"), ("Wuwei", "Gansu"), ("Jiuquan", "Gansu"),
("Banyin", "Gansu"), ("Pingliang", "Gansu"), ("Jiayuguan", "Gansu"), ("Jinchang", "Gansu"), ("Gannan", "Gansu"),

("Xining", "Qinghai"), ("Haixi", "Qinghai"), ("Haidong", "Qinghai"), ("Haibei", "Qinghai"), ("Guoluo", "Qinghai"),
("Yushu", "Qinghai"),

("Wulumuqu", "Xinjiang"), ("Yili", "Xinjiang"), ("Changji", "Xinjiang"), ("Shihezi", "Xinjiang"), ("Hami", "Xinjiang"),
("Asuke", "Xinjiang"), ("Keshi", "Xinjiang"), ("Hetian", "Xinjiang"), ("Tulufan", "Xinjiang"), ("Alaer", "Xinjiang"),

("Lasa", "Xizang"), ("Shannan", "Xizang"), ("Linzhi", "Xizang"), ("Rikaze", "Xizang"), ("Ali", "Xizang"),
("Changdu", "Xizang"), ("Naqu", "Xizang"),

("Jilin", "Jilin"), ("Changchun", "Jilin"), ("Baishan", "Jilin"), ("Yanbian", "Jilin"), ("Baicheng", "Jilin"),
("Songyuan", "Jilin"), ("Tonghua", "Jilin"), ("Siping", "Jilin"),

("Yinchuan", "Ningxia"), ("Wuzhong", "Ningxia"), ("Zhongwei", "Ningxia"), ("Shizuishan", "Ningxia"), ("Guyuan", "Ningxia"),
]

import requests
import json
import random
import string

url = "http://127.0.0.1:3579/create/"
header_dict = {"Content-Type": "application/json; charset=utf8"}

def name_generator():
	return ''.join(random.choice(string.ascii_letters) for _ in range(10))

def age_generator():
	return random.randint(0, 150)

def city_province_pair_generator():
	return random.choice(city_province_pairs)

def phone_generator():
	return random.randint(1, 99999999999)

for _ in range(10000):
	city_province_pair = city_province_pair_generator()
	person = {"name": name_generator(), "age": age_generator(), "city": city_province_pair[0], "province": city_province_pair[1], "phone": phone_generator()}
	str_person = json.dumps(person)
	try:
		requests.post(url, data=str_person, headers = header_dict)
	except:
		pass
