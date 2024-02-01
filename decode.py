import stepic
from PIL import Image

file=input("Photo: ")

img=Image.open(file)
decode=stepic.decode(img)
print("The signature is : "+ str(decode))