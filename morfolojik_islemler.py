import cv2
import numpy as np

img = cv2.imread("Helikopter.jpg",0)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations=5) #kalınlaştırma
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  #resim üzerindeki gürültü kaldırma
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  #nesne içindeki gürültü düzeltme
gardient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT, kernel)  #nesnenin dışı çizili içi siyah olarak bırakır
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel )


cv2.imshow("img",img)
cv2.imshow("dilation ",dilation )
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.imshow("gardient", gardient)
cv2.imshow("tophat", tophat)



cv2.waitKey(0)
cv2.destroyAllWindows()