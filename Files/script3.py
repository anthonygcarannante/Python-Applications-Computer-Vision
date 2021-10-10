import cv2

# https://stackoverflow.com/questions/30508922/error-215-empty-in-function-detectmultiscale
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread("/Users/anthonycarannante/Desktop/Github_Repos/Python-Applications-Computer-Vision/Files/photo.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05)

print(type(face))

cv2.imshow("Gray",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
