import cv2 
import pytesseract
import numpy as np
from PIL import Image
import os.path

image_array = ['img1.jpeg','img2.jpeg','img3.jpeg','img4.jpeg','img5.jpg','img6.jpg','img7.jpg','img8.jpg','img9.jpg','img10.jpg','img11.jpeg']

for i,imgs in enumerate(image_array):
    img = cv2.imread(imgs)
    WIDTH = 2586
    HEIGHT = 3725
    dim = (WIDTH,HEIGHT)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   

    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    #cv2.imshow('d',img)
    #cv2.waitKey(0) 
    
    #cv2.imwrite("Image%i.png" %i,img)
    #im = Image.open("Image%i.png"%i)
    #im.save("Image1%i.tiff",dpi=(300.0,300.0))
    #img1 = cv2.imread("Image1%i.tiff")
    p =pytesseract.image_to_string(img) 
    print(p)
   

    w = open('IPi%i.txt' %i,'w')
    f = w.write(p)
    w.close


