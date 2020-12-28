import requests
from PIL import Image
from io import BytesIO

r = requests.get("https://displate.com/images/blog/0a2f80ee23b7acb268c1a7b0f9bdd309b7db69e8/400x267%20Rutkowski.jpg")

print(r.status_code)

img = Image.open(BytesIO(r.content)) # type: Image.Image
print(img.size, img.format, img.mode)

img_path = "./img." + img.format

try:
    img.save(img_path, img.format)
    print("image saved");
except IOError:
    print("can't download iamge")


