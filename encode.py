import stepic
from PIL import Image
key='This is the signature'
file=input("file: ")

img=Image.open(file)

img_stegano=stepic.encode(img, key.encode())
img_stegano.save("img.png")