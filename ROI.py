#BİR RESİMDEKİ YÜZ İLE İLGİLENİYORSAK ROİ MİZ YÜZDÜR.
#roi -->region of interest -->ilgi alanı

#klon askerin yüzünü diğer vucüt resimlerden ayırma

import  cv2
img = cv2.imread("klon.jpg")

roi = img[30:200, 200:400]

cv2.imshow("Klon", img)
cv2.imshow("ROI", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()