import cv2

# Define variable for first frame with "None" value to call later
first_frame = None

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    print(first_frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Smooths out blurs in image
    gray = cv2.GaussianBlur(gray, (21,21), 0)
    print(gray)

    if first_frame is None:
        first_frame = gray
        continue

    # Difference between first frame and current frame
    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)


    print(delta_frame)
    
    # Compare blurry and gray-scaled image
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)

    key=cv2.waitKey(1)

    # Capture video. If captured,
    if key == ord('q'):
        break

# Print number of frames captured
video.release()
cv2.destroyAllWindows()