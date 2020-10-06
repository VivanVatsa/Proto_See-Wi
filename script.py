import cv2

# 0 = black image
# -1 = color image
img = cv2.imread("galaxy.jpg", 1)

print(type(img))
print(img)
# image resolution

print(img.shape)
print(img.ndim)

cv2.imshow("Galaxy", img)
# cv2.waitKey(2000) #this acts in milliseconds
cv2.waitKey(0)
cv2.destroyAllWindows()