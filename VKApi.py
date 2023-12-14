import requests


class Vk_action:

    url = 'https://api.vk.ru/method'

    def __init__(self, token):
        self.token = token[0]
        self.user_id = token[1]

    def info_params(self):
        return {'access_token': self.token,
                  'v': '5.131'
                }

    def receipt_info_photos(self):
        params = self.info_params()
        params.update({'user_id': self.user_id, 'album_id': 'profile', 'extended': 1})
        responce = requests.get(f'{self.url}/photos.get', params=params)
        return responce.json()

