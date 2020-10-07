import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# img=cv2.imread("photo.jpg", 0)
img=cv2.imread("photo.jpg")

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

faces=face_cascade.detectMultiScale(gray_img, 
                                    scaleFactor=1.05,
                                    minNeighbors=5)

print(type(faces))
print(faces)


cv2.imshow("Gray Image", gray_img)
cv2.waitKey(0)
# 0 is for press any key when the window run then it closes
cv2.destroyAllWindows()