import cv2

# 0 = black image
# -1 = color image
img = cv2.imread("galaxy.jpg", 1)

print(type(img))
print(img)
# image resolution

print(img.shape)
print(img.ndim)

# the pixels too big to fit in the window so gotta resize eh

# resized_image = cv2.resize(img,(500, 700))
resized_image = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
# cv2.imshow("Galaxy", img)
cv2.imshow("Galaxy", resized_image)
# cv2.waitKey(2000) #this acts in milliseconds
cv2.waitKey(0)
cv2.destroyAllWindows()