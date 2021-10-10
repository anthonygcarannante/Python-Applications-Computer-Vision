import cv2

# https://stackoverflow.com/questions/30508922/error-215-empty-in-function-detectmultiscale
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread("/Users/anthonycarannante/Desktop/Github_Repos/Python-Applications-Computer-Vision/Files/news.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Look for face using xml file
face = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05)

# Draw rectangle around the detected face
for x,y,w,h in face:
    img=cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,0), 3)

print(type(face))
print(face)

resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
