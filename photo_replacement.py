import requests
import os
import random
import shutil

name_files = []

for root, dirs, files in os.walk( folder with unwanted photos ):
    for file in files:
        if file.endswith(".jpg") or file.endswith('.png') or file.endswith('.gif'):
            path_file = os.path.join(root,file)
            name_files.append(path_file.split('\\')[-1])
            
letters = 'qwertyuiopasdfghjklzxcvbnm1234567890'

while True:
    url_input = input('Enter photo URL: ')
    location = input('Enter photo location: ')
    r = requests.get(url_input)
    if r.status_code == 200:
        file_name = random.choice(name_files)
        with open(location.replace('\\', '\\\\'), 'wb') as open_file:
            open_file.write(r.content)
            
        new_name_file = ''
        for i in range(5):
            new_name_file += random.choice(letters)
            
        shutil.move(f'C:\\path photo\\{file_name}',
                    f'C:\\new path photo\\{new_name_file}.'
                    f'{file_name.split(".")[-1]}')
        print(f'Successfully. File moved to main screen. {new_name_file}.{file_name.split(".")[-1]}\n')

    else:
        print('\nconnection error\n')
