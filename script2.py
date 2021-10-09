import cv2
import glob
import os

# Read image: (1: read as rbg, 0: read as greyscale, -1: color img with transparancy)
images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image,0)
    re_img = cv2.resize(img, (100,100))
    cv2.imshow("Image", re_img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
    cv2.imwrite(f"resized{image}", re_img)
