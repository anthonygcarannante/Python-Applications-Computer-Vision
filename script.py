import cv2

# Read image: (1: read as rbg, 0: read as greyscale, -1: color img with transparancy)
img = cv2.imread('galaxy.jpg', 0)

# Image is a Numpy array
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

# Resize & Display Image
resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)

# Write image to new file 
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()