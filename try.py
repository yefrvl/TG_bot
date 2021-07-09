import requests
from bs4 import BeautifulSoup
import re
def get_full_info_others(items_id_array):

    for item in items_id_array:
        url_for_search = f'https://www.wildberries.ru/catalog/{item}/detail.aspx'
        responce_url = requests.get(url_for_search)
        get_responce_url = BeautifulSoup(responce_url.text, 'lxml')
        name = re.findall('<meta content="(.*)" itemprop="name"\/>', str(get_responce_url))
        image_url = re.findall('<meta content="(.*)" itemprop="image"\/>', str(get_responce_url))
        price = re.findall('<meta content="(.*)" itemprop="price"\/>', str(get_responce_url))
        #print(url_for_search, item, name, price, image_url)
        size = get_responce_url.findAll('label', class_='disabled')
        return [dis_size.find('span').text for dis_size in size]

print(get_full_info_others([18097679]))