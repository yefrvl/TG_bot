import requests
import re
import json
from bs4 import BeautifulSoup


def get_name_to_look():
    name_to_look = input('Введите наименование искомого товара: ')
    return name_to_look

def pars_wildberies_items(name_for_search):
    first_url_for_search = f'https://wbxsearch.wildberries.ru/suggests/male?query={name_for_search}'
    responce_first_url = requests.get(first_url_for_search)
    get_responce_firs_url = BeautifulSoup(responce_first_url.text, 'lxml')
    get_query_item = re.findall('"query":"(.*)","name', str(get_responce_firs_url))
    second_url_for_search = f'https://wbxcatalog-ru.wildberries.ru/presets/bucket_139/catalog?spp=15&' \
                  f'regions=64,79,4,38,30,33,70,1,22,31,66,40,69,80,48,68&stores=119261,122252,' \
                  f'122256,121631,122466,122467,122495,122496,122498,122590,122591,122592,123816,123817,' \
                  f'123818,123820,123821,123822,124096,124097,124098,124583,124584,118019,1699,116433,117501,' \
                  f'507,3158,120762,119400,117986,2737,117413,119781&pricemarginCoeff=1.0&reg=1&appType=1&' \
                  f'offlineBonus=0&onlineBonus=0&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=2,6,7,3,19,21,8&' \
                  f'{get_query_item[0]}&xfilters=xsubject%3Bdlvr%3Bbrand%3Bprice%3Bkind%3Bcolor%3Bwbsize%3Bseason%3' \
                  f'Bconsists&xparams=preset%3D10946560&xshard=presets%2Fbucket_139&'
    responce_second_url = requests.get(second_url_for_search)
    get_responce_second_url = BeautifulSoup(responce_second_url.text, 'lxml')
    row_items = re.findall(r'data":(.*)}<\/p>', str(BeautifulSoup(get_responce_second_url.text, 'lxml')))
    row_dict_items = json.loads(row_items[0])
    return row_dict_items['products']


def price_items():
    ready_array = []
    items_array = pars_wildberies_items(get_name_to_look())


    for item in items_array:
        ready_array.append(item.get('id'))
    return ready_array

print(price_items())







