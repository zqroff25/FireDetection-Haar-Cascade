import cv2

img=cv2.imread("yangin.jpg")
yangin_cascade=cv2.CascadeClassifier("yangin_cascade\\yangin_cascade.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

yangin=yangin_cascade.detectMultiScale(gray,5,8)

for(x,y,w,h) in yangin:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()