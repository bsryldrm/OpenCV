import cv2
import numpy as np

img = cv2.imread("klon.jpg")

dimension = img.shape
print(dimension)#pikselin kaça kaçlık olduğunu çıktısı

color = img[205,200] #pikselin rengini sorarız
print("BGR: ", color)

blue = img[420,500, 0]
print("BLUE: ", color)

green = img[420,500, 1]
print("GREEN: ", color)

red = img[420,500, 2]
print("RED: ", color)

img[420, 500, 0] = 250
print("new blue: ", img[420, 500, 0])

blue1 = img.item(150, 200, 0)
print("blue1: ", blue1)

img.itemset((150, 200, 0), 172)
print("nem blue1: ", img[150,200,0])

cv2.imshow("klon Asker", img)
cv2.waitKey(0)
cv2.destroyAllWindows()