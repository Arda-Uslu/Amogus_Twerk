import cv2
from playsound import playsound

img1=cv2.imread("p1.png",1)
img2=cv2.imread("p3.png",0)
img3=cv2.imread("p2.png",1)
img4=cv2.imread("p4.png",0)

# 50 cent x eminem at 9 pm farting section

while(1):
    cv2.imshow("a",img1)
    cv2.waitKey(100)
    cv2.imshow("a",img2)
    cv2.waitKey(100)
    cv2.imshow("a",img3)
    cv2.waitKey(100)
    cv2.imshow("a",img4)
    cv2.waitKey(100)

cv2.waitKey(0)
cv2.destroyAllWindows()
