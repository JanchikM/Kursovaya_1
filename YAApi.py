import requests
import logging


class Ya_action:

    url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, token_ya, folder_name):
        self.token_ya = token_ya[0]
        self.folder = self.add_folder(folder_name)

    def info_autorization(self):
        return {'Authorization': self.token_ya}

    def add_folder(self, folder_name):
        params = {'path': folder_name}
        headers = self.info_autorization()
        responce = requests.put(f'{self.url}', params=params, headers=headers)
        if responce.status_code in range(200, 300):
            logging.info(f'\nПапка {folder_name} успешно создана\n')
        else:
            logging.info(f'\nПапка с таким названием уже существует.\n')
        return folder_name

    def add_photo(self, dict_info, total):
        self.total = total
        counter = 0
        for key in dict_info:
            if counter < self.total:
                params = {'path': f'{self.folder}/{key}',
                      'url': dict_info[f'{key}']}
                headers = self.info_autorization()
                responce = requests.post(f'{self.url}/upload', params=params, headers=headers)
                counter += 1
                if responce.status_code in range(200, 300):
                    logging.info(f'\nФаил с названием {key} успешно скопирован\n')
                else:
                    logging.info(f'\nКопирование не удалось\n')

