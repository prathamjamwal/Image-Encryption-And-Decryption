
import matplotlib.pyplot as aj ,random
from numpy import zeros
import numpy as ny
print("Welcome to image encription project")
x= input('Give the jpg image. : ')
img=aj.imread(x)
rows=img.shape[0]
col=img.shape[1]

aj.title("Genuine Image")
aj.imshow(img)
aj.show()
key=[]
while len(key)!=256:
    j=random.randrange(0,256)
    if j not in key:
        key.append(j)
dKey = key[0]

def encrypt_image(img, key, rows, col):

    img1=ny.zeros((rows,col,3),dtype=int)
    for i in range(rows):
        for j in range(col):
            for k in range(3):
                img1[i][j][k]=key[img[i][j][k]]
    return img1
e = (int)(input('Enter 0 to begin Encryption :'))
if(e==0):
    print('Encryption key for the image is : ',key[0])
    print("Starting Encryption")
    img1=encrypt_image(img,key,rows,col)
a, b, c = img1[:,:,0], img1[:,:,1], img1[:,:,2]
grayimage = 0.2989 * a + 0.5870 * b + 0.1140 * c
aj.imshow(grayimage, cmap='gray')
aj.title("Encrypted")
aj.show()
def decrypt_image(img,key, rows, col):
    img1=ny.zeros((rows,col,3),dtype=int)
    for i in range(rows):
        for j in range(col):
            for k in range(3):
                img1[i][j][k]=key.index(img[i][j][k])
    return img1

o = (int)(input('Enter 1 to begin decryption : '))
if(o==1):
    d= (int)(input("Enter key if you want to begin decryption : "))
    if(d == dKey):

        img3=decrypt_image(img1,key,rows,col)
        aj.title("Decrypted Image")
        aj.imshow(img3)
        aj.show()