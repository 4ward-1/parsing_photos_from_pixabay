import requests
import random
from PIL import Image
import io

# Программа скачивает и сохраняет N случайных картинок заданного наименования с сайта pixabay.com
i = 0
N = 10
# pixabay key
API_KEY = '37513888-d05009ec246b05b69b893b520'
image_to_find = 'warship'
url = f'https://pixabay.com/api/?key={API_KEY}&q={image_to_find}&image_type=photo'

response = requests.get(url)
data = response.json() # готовая функция для парсинга ответов в формате json

while i < N:
    i += 1
    random_hit = random.choice(data['hits'])
    image_url = random_hit['largeImageURL']
    image_data_bytes = requests.get(image_url).content
    image = Image.open(io.BytesIO(image_data_bytes))
    image.save('{0}_{1}.jpg'.format(image_to_find, i))