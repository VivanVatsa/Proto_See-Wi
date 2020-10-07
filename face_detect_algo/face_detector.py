import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# img=cv2.imread("photo.jpg", 0)
img=cv2.imread("photo.jpg")

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

faces=face_cascade.detectMultiScale(gray_img, 
                                    scaleFactor=1.05,
                                    minNeighbors=5)


for x,y,w,h in faces:
    img=cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
    # third tuple argument is for RGB color
    
print(type(faces))
print(faces)


resized=cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

# cv2.imshow("Gray Image", gray_img)
# cv2.imshow("Gray Image",img)
cv2.imshow("Gray Image",resized)
cv2.waitKey(0)
# 0 is for press any key when the window run then it closes
cv2.destroyAllWindows()