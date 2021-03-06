# cv2.Canny(input,minThreshold,maxThreshold)

import cv2

cap = cv2.VideoCapture(0)

while 1:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    edges = cv2.Canny(frame,50,200) #100,200 --> min. max. eşik değerleri

    cv2.imshow("Frame",frame)
    cv2.imshow("Edges",edges)

    if cv2.waitKey(5) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
