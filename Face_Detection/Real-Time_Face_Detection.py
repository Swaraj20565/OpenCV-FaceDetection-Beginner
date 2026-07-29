import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
else:
    print("Webcam opened successfully!")

    while True:
        # Capture one frame
        ret, frame = cap.read()

        # If frame is not captured
        if not ret:
            break

       
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
       )
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5
      )
        for (x, y, w, h) in faces:
          cv2.rectangle(
          frame,
          (x, y),
          (x + w, y + h),
          (0, 255, 0),
          2
       )
           # Display the frame
        cv2.imshow("Webcam", frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the webcam
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()



# 1. Open the default webcam

# 2.  show imgshow  in loop 

# 3.  if ( ! return_value )  - break loop

#      else - frame by frame show (until press 'q')

# 4. 

