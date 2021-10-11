import cv2, time

# Define variable for first frame with "None" value to call later
first_frame = None

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Smooths out blurs in image
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    print(gray)
    print(first_frame)

    # Compare blurry and gray-scaled image
    delta_frame = cv2.absdiff(first_frame, gray)

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)

    key=cv2.waitKey(1)
    
    # Capture video. If captured,
    if key == ord('q'):
        break

# Print number of frames captured
video.release()
cv2.destroyAllWindows()