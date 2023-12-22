from VKApi import *
from YAApi import *
from add_token import *
import datetime
import json
import os


# Логирование
logging.basicConfig(level=logging.INFO, filename="log_save_file.log",
                    encoding='utf-8', filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

# Функция чтения токенов
def get_token(file_name):
    with open(os.path.join(os.getcwd(), file_name), 'r') as f:
        token = f.readline().strip()
        user_id = f.readline().strip()
    return token, user_id

# Функция определения максимальных размеров
def max_size():
    count_url = []
    count_type = []
    for i in vk_app.receipt_info_photos()['response']['items']:
        x = max(i['sizes'], key=lambda x:x['width'] * x['height'])
        count_url.append(x['url'])
        count_type.append(x['type'])
    return count_url, count_type

# Функция преобразования форматов дат
def time_convert(time_unix):
    time_bc = datetime.datetime.fromtimestamp(time_unix)
    str_time = time_bc.strftime('date_%Y-%m-%d time_%H-%M-%S')
    return str_time

# Функция создания названий
def likes_date():
    count_likes = []
    for l in vk_app.receipt_info_photos()['response']['items']:
        likes = l['likes']['count']
        time = time_convert(l['date'])
        file_name = f'{likes}_Likes {time}'
        count_likes.append(file_name)
    return count_likes

# Функция создания словаря с названиями и url
def dict_info():
    dict_file = {}
    dict_file = dict(zip(likes_date(), max_size()[0]))
    return dict_file

# Функция создания json файла
def info_json():
    dict_albums = {}
    save_file_json_all = []
    dict_albums = dict(zip(likes_date(), max_size()[1]))
    for i in dict_albums.items():
        save_file_json = {}
        save_file_json['file_name'] = f'{i[0]}.jpg'
        save_file_json['size'] = i[1]
        save_file_json_all.append(save_file_json)
    with open('save_file.json', 'w') as f:
        json.dump(save_file_json_all, f, ensure_ascii=False, indent=2)
    return save_file_json_all

token_vk = 'infoVK.txt'
token_ya = 'info_ya.txt'
add_tok_vk = add_token_vk()
add_tok_ya = add_token_ya()
vk_app = Vk_action(get_token(token_vk))
logging.info(f'\nСловарь с названиями и ссылками на фотографии сформирован')
ya_client = Ya_action(get_token(token_ya), input('Введите название папки: '))
ya_client.add_photo(dict_info(), int(input('Введите колличество загружаемых фото: ')))
save_file_json_all = info_json()
