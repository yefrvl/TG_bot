import requests
import re
import json
from bs4 import BeautifulSoup
from config import first_url_array

def get_first_url(url_array, i=0):

    name_for_search = 'xbox+series+x'

    if len(url_array) == 0:
        return

    else:
        item = url_array.pop(0)
        first_url_for_search = f'{item}{name_for_search}'
        responce_first_url = requests.get(first_url_for_search)
        get_responce_first_url = BeautifulSoup(responce_first_url.text, 'lxml')
        get_for_bool = re.findall(r'<p>(.*)', str(get_responce_first_url))
        get_for_bool_type_item = json.loads(str(get_for_bool[0]))
        if bool(get_for_bool_type_item) == True:
            return get_responce_first_url
        return get_first_url(url_array)

print(get_first_url(first_url_array))