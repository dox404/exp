import stepic
from PIL import Image
key='this is the embeded text'
file=input("file: ")

img=Image.open(file)

img_stegano=stepic.encode(img, key.encode())
img_stegano.save("img.png")