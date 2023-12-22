def add_token_ya():
    with open('info_ya.txt', 'w') as f:
        token = f.write(input('Введите ваш токен Яндекс Диска: '))

def add_token_vk():
    with open('infoVK.txt', 'w') as f:
        token = f.write(input('Введите ваш токен VK:') + '\n')
        user_id = f.write(input('Введите ваш ID: '))