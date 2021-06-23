import requests
import re
import json
from bs4 import BeautifulSoup
from config import first_url_array

def replace_space_to_plus(name):

    name_for_search = re.sub(r'( )', '+', name)
    return name_for_search

def get_first_url(iteracion, name_for_search, url_array):


    name_for_search = replace_space_to_plus(name_for_search)

    for url in url_array:
        first_url_for_search = f'{url}{name_for_search}'
        if first_url_array == True:
            return first_url_for_search
        else:
            get_first_url(iteracion+1, name_for_search, url_array[iteracion+1:])


"""
    try:
        first_url_for_search = f'https://wbxsearch.wildberries.ru/suggests/male?query={name_for_search}'
        return first_url_for_search
    except bool(False):
        first_url_for_search = f'https://wbxsearch.wildberries.ru/exactmatch/v2/male?query={name_for_search}'
        return first_url_for_search
    except bool(False):
        first_url_for_search = f'https://www.wildberries.ru/search/exactmatch/male?query={name_for_search}'
        return first_url_for_search
"""



def pars_wildberies_items(name_for_search):

    first_url_for_search = get_first_url(0, name_for_search, first_url_array)
    responce_first_url = requests.get(first_url_for_search)
    get_responce_firs_url = BeautifulSoup(responce_first_url.text, 'lxml')
    get_query_item = re.findall('"query":"(.{15})","name', str(get_responce_firs_url))
    get_query_shardkey = re.findall('shardKey":"(.{10,25})","filters', str(get_responce_firs_url))
    print(get_query_item, get_query_shardkey)
    second_url_for_search = f'https://wbxcatalog-ru.wildberries.ru/{get_query_shardkey[0]}/catalog?spp=15&' \
                  f'regions=64,79,4,38,30,33,70,1,22,31,66,40,69,80,48,68&stores=119261,122252,' \
                  f'122256,121631,122466,122467,122495,122496,122498,122590,122591,122592,123816,123817,' \
                  f'123818,123820,123821,123822,124096,124097,124098,124583,124584,118019,1699,116433,117501,' \
                  f'507,3158,120762,119400,117986,2737,117413,119781&pricemarginCoeff=1.0&reg=1&appType=1&' \
                  f'offlineBonus=0&onlineBonus=0&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=2,6,7,3,19,21,8&' \
                  f'{get_query_item[0]}'
    print(second_url_for_search)
    responce_second_url = requests.get(second_url_for_search)
    get_responce_second_url = BeautifulSoup(responce_second_url.text, 'lxml')
    print(get_responce_second_url)

    try:
        row_items = re.findall(r'data":(.*)}<\/p>', str(BeautifulSoup(get_responce_second_url.text, 'lxml')))
        row_dict_items = json.loads(row_items[0])
        return row_dict_items['products']

    except IndexError:
        row_items = re.findall(r'"query":"(.*)",', str(BeautifulSoup(get_responce_second_url.text, 'lxml')))
        return row_items



def get_items_id_dict(name_for_search):

    items_id_array = pars_wildberies_items(name_for_search)
    return [x.get('id') for x in items_id_array]


def get_full_info_dict_items(text):
    items_id_array = get_items_id_dict(text)
    for item in items_id_array:
        url_for_search = f'https://www.wildberries.ru/catalog/{item}/detail.aspx'
        responce_url = requests.get(url_for_search)
        get_responce_url = BeautifulSoup(responce_url.text, 'lxml')
        name = re.findall('<meta content="(.*)" itemprop="name"\/>', str(get_responce_url))
        image_url = re.findall('<meta content="(.*)" itemprop="image"\/>', str(get_responce_url))
        price = re.findall('<meta content="(.*)" itemprop="price"\/>', str(get_responce_url))
        return url_for_search, item, name, price, image_url


#print(get_full_info_dict_items())







