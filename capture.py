import cv2, time

video = cv2.VideoCapture(0)

# Iterator value for number of frames captured
a = 1

while True:
    a = a+1
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)

    key=cv2.waitKey(1)
    
    # Capture video. If captured,
    if key == ord('q'):
        break

# Print number of frames captured
print(a)
video.release()
cv2.destroyAllWindows()