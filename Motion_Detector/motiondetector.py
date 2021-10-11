import cv2, time

# Define variable for first frame with "None" value to call later
first_frame = None

video = cv2.VideoCapture(0)
time.sleep(2)

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Smooths out blurs in image
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    # Difference between first frame and current frame
    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Estimate contours on threshold image
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate and check if contour area is less than 1000 pixels. If so, go to the next contour
    for contour in cnts:
        if cv2.contourArea(contour) < 100:
            continue
        
        # If contour is greater than 1000 pixels, draw rectangle around it.
        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    # Compare blurry and gray-scaled image
    cv2.imshow("Color Frame", frame)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)

    key=cv2.waitKey(1)

    # Capture video. If captured,
    if key == ord('q'):
        break

# Print number of frames captured
video.release()
cv2.destroyAllWindows()