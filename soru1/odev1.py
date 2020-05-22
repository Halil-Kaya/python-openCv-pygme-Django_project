import cv2

img = cv2.imread("index.jpeg")
img = cv2.resize(img,(500,500))
img = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
img = cv2.medianBlur(img,9)


font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,"Halil Ibrahim Kaya",(10,450), font, .9,(0,255,0),2,cv2.LINE_AA)
cv2.imshow("frame",img)


key = cv2.waitKey(0)

if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()

