import os
import requests
from urllib.request import urlretrieve
os.makedirs('./img/', exist_ok=True)
image_url = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
# urlretrieve(image_url, '/.image/image1.png')
r = requests.get(image_url)
with open('./img/image2.png', 'wb') as f:
    f.write(r.content)

r = requests.get(image_url, stream=True)
with open('./img/image2.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
