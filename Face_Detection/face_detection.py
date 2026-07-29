import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Cannot open webcam")
else:
    print("Webcam opened successfully!")
    ret, frame = cap.read()   # cap.read() captures one image (one frame) from the webcam.
    print(ret)
# /*
#          Webcam
#            │
#            ▼
#        cap.read()
#            │
#      ┌─────┴─────┐
#      ▼           ▼
#    ret         frame
    # (True/False) (Captured Image)
# 
 
    if ret:
      print("Frame captured")
      print(frame)
      print(type(frame))

      # Grayscale Image (1 Channel):Only Light and Dark
      # We convert to grayscale because it removes color information, making face detection faster and more efficient.
      
      # Interview Answer (30 seconds)
         # "We convert the image to grayscale because color information is not required for face detection. 
         # Grayscale reduces the image from three color channels to one, making processing faster and allowing
         # The Haar Cascade algorithm to detect faces more efficiently."

      # Grayscale has only one channel, so it:
        # ✅ Reduces data
        # ✅ Speeds up processing
        # ✅ Improves face detection performance

      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


      if gray is not None:
        print("Yes, converted to Grayscale.")
        # Haar Cascade is a pre-trained OpenCV model that detects faces (or other objects) in an image.
        face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        if len(faces) > 0:
           print('face Detected ....')
           
        else:
           print('Not Face Detect ....')
        for (x, y, w, h) in faces:
                            cv2.rectangle(
                              frame,
                              (x, y),
                              (x + w, y + h),
                              (0, 255, 0),
                              2
                            )

        # cv2.rectangle(image, start_point, end_point, color, thickness) ....
        cv2.imshow("Captured Image", frame)
        
        cv2.waitKey(0)  # Wait until a key is pressed
      else:
        print("Conversion failed.")
    else:
       print("Frame not captured")

# Release the webcam
cap.release()
cv2.destroyAllWindows()