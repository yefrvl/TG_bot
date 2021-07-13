import shelve
import pandas as pd
def create_tmp_shelve_db(user_id, item_array):
    with shelve.open("temp_db") as items:
        return {user_id:{str(item):f'https://www.wildberries.ru/catalog/{item}/detail.aspx'} for item in item_array}

print(create_tmp_shelve_db('45646456',[18097678, 18097680, 18097683, 18097679, 18097682, 18097681, 18097665, 18097651, 18097653, 13749514, 13749473, 18097742, 18097741, 18097654, 13749516, 16213687, 10502343, 16213678]))