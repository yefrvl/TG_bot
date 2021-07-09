import requests
import re
import json
from bs4 import BeautifulSoup
from config import url_array

def replace_space_to_plus(name):

    """Функция посредством регулярного выражения заменяет пробелы на знак плюса
    в переменной ссылки для поиска"""

    search_name = re.sub(r'( )', '+', name)
    return search_name

def get_first_url(name_for_search, url_array, i=0):

    """Функция с помощью регулярного выражения ищет подходящую по определенным аргуменам переменную,
    проверяет её по длине и возвращает в функцию парсинга """

    name_for_search_with_plus = replace_space_to_plus(name_for_search)

    if len(url_array) == 0:
        return

    else:
        item = url_array.pop(0)
        first_url_for_search = f'{item}{name_for_search_with_plus}'
        responce_first_url = requests.get(first_url_for_search)
        get_responce_first_url = BeautifulSoup(responce_first_url.text, 'lxml')
        get_for_bool = re.findall(r'<p>(.*)<\/p>', str(get_responce_first_url), re.S)
        if len(str(get_for_bool)) < 5:
            return get_first_url(url_array)
        get_for_bool_type_item = json.loads(str(get_for_bool[0]))
        return get_for_bool_type_item


def pars_wildberies_items(name_for_search):

    get_responce_from_first_url = get_first_url(name_for_search, url_array)

    if 'preset=10204659' not in get_responce_from_first_url:
        second_url_for_search = f'https://www.wildberries.ru/search/extsearch/catalog?spp=15&' \
                                f'regions=64,79,4,38,30,33,70,1,22,31,66,40,69,80,48,68&stores=119261,122252,122256,' \
                                f'121631,122466,122467,122495,122496,122498,122590,122591,122592,123816,123817,123818,' \
                                f'123820,123821,123822,124096,124097,124098,124583,124584,118019,1699,116433,117501,' \
                                f'507,3158,120762,119400,117986,2737,117413,119781&pricemarginCoeff=1.0&reg=1&' \
                                f'appType=1&offlineBonus=0&onlineBonus=0&emp=0&locale=ru&lang=ru&curr=rub&' \
                                f'couponsGeo=2,6,7,3,19,21,8&search={replace_space_to_plus(name_for_search)}'

    else:
        get_query_item = re.findall("{'query': '(.{15})', 'name':", str(get_responce_from_first_url))
        get_query_shardkey = re.findall("'shardKey': '(.{10,25})', 'filters':", str(get_responce_from_first_url))

        second_url_for_search = f'https://wbxcatalog-ru.wildberries.ru/{get_query_shardkey[0]}/catalog?spp=15&' \
                      f'regions=64,79,4,38,30,33,70,1,22,31,66,40,69,80,48,68&stores=119261,122252,' \
                      f'122256,121631,122466,122467,122495,122496,122498,122590,122591,122592,123816,123817,' \
                      f'123818,123820,123821,123822,124096,124097,124098,124583,124584,118019,1699,116433,117501,' \
                      f'507,3158,120762,119400,117986,2737,117413,119781&pricemarginCoeff=1.0&reg=1&appType=1&' \
                      f'offlineBonus=0&onlineBonus=0&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=2,6,7,3,19,21,8&' \
                      f'{get_query_item[0]}'

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
    return items_id_array

def get_full_info_others(items_id_array):
    for item in items_id_array:
        url_for_search = f'https://www.wildberries.ru/catalog/{item}/detail.aspx'
        responce_url = requests.get(url_for_search)
        get_responce_url = BeautifulSoup(responce_url.text, 'lxml')
        name = re.findall('<meta content="(.*)" itemprop="name"\/>', str(get_responce_url))
        image_url = re.findall('<meta content="(.*)" itemprop="image"\/>', str(get_responce_url))
        price = re.findall('<meta content="(.*)" itemprop="price"\/>', str(get_responce_url))
        return url_for_search, item, name, price, image_url

def get_full_info_shoes(items_id_array):
    for item in items_id_array:
        url_for_search = f'https://www.wildberries.ru/catalog/{item}/detail.aspx'
        responce_url = requests.get(url_for_search)
        get_responce_url = BeautifulSoup(responce_url.text, 'lxml')
        name = re.findall('<meta content="(.*)" itemprop="name"\/>', str(get_responce_url))
        image_url = re.findall('<meta content="(.*)" itemprop="image"\/>', str(get_responce_url))
        price = re.findall('<meta content="(.*)" itemprop="price"\/>', str(get_responce_url))











