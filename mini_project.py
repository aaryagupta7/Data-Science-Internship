import cv2

#Define a object to access the webcam
ob = cv2.VideoCapture(0)

#Check if the camera is opened successfully
if not ob.isOpened():
    print("Error")
    exit()

#Variables for gesture detection
background = None
accumulated_weight = 0.5    
gesture_flag = False

#Loop to continuously capture and process video
while True:
    ret, frame = ob.read()

    if not ret:
        print("Error: Could not read a frame.")
        break
    #Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21,21),0)

    if background is None:
        background = gray_frame.copy().astype("float")
        continue

    #Calculate the absolute difference between the current frame and the background frame
    cv2.accumulateWeighted(gray_frame, background, accumulated_weight) 
    frame_delta = cv2.absdiff(gray_frame, cv2.convertScaleAbs(background))

    #Apply thresholding to the frame
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    #Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            #Adjust the area threshold as needed
            continue

        #Gesture recognition by movement
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        gesture_flag = True

    #Display frmae in a window
    cv2.imshow("Video", frame) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

#Close the window
ob.release()
cv2.destroyAllWindows()    


