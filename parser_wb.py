import requests
import re
import json
from bs4 import BeautifulSoup


def get_name_to_look():

    name_to_look = input('Введите наименование искомого товара: ')
    return name_to_look

def pars_wildberies_items(name_to_look):


    url_to_look = f'https://www.wildberries.ru/catalog/0/search.aspx?search={name_to_look}&xsearch=true'

    responce = requests.get(url_to_look)
    get_responce = BeautifulSoup(responce.text, 'lxml')
    print(get_responce)
    row_items = re.findall(r'shortProducts:(.*), nms:',
                           str(BeautifulSoup(responce.text, 'lxml').find_all('script', type='text/javascript')))
    """print(row_items[0])
    row_dict_items = json.loads(row_items[0])

    return dict.keys(row_dict_items)"""


def price_items():
    pass

print(pars_wildberies_items(get_name_to_look()))


