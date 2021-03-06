import cv2
import numpy as np
from matplotlib import pyplot as plt                  # eğer yüklü değilse, cmd --> pip install matplotlib

img = cv2.imread("smile.jpg")
b,g,r = cv2.split(img)
cv2.imshow("img",img)

plt.hist(b.ravel(),256,[0,256])  #plt.hist fonk. ile histogramı mızı çizdirip
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

plt.show()   #plt.show fonk. ile de gösterebiliriz


cv2.waitKey(0)
cv2.destroyAllWindows()
