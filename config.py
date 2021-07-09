from enum import Enum
token = '1761116546:AAHi5egtNSa0uNjuni5mAbifizTE8qKLTXU'


url_array = ['https://wbxsearch.wildberries.ru/suggests/male?query=', 'https://wbxsearch.wildberries.ru/exactmatch/v2/male?query=',
                   'https://www.wildberries.ru/search/exactmatch/male?query=']
size_array_euro = ['5', '5H', '6', '6H', '7', '7H', '8', '8H', '9', '9H', '10', '10H', '11', '11H', '12']
size_array_ru = ['36', '37', '38', '40', '41']
size_array_sl = ['35/5', '36/6', '37/7', '38/8', '39/9', '39-40/9', '41-42/10', '41/11', '11', '42-43/11', '42-43', '43']


class States(Enum):
    S_START = 0
    S_CHOICE_TYPE_ITEM = 1
    S_FIND = 2
    S_ADD_FAVORIT = 3


