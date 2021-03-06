# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV 
import cv2
import time
 
# marginal values for buzzer activation
left = int((320/3))
half = int(320/2)
right = int(320*2/3)
print left,  half, right

# capture frames from a video
cap = cv2.VideoCapture("video33.3gp")
 
# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')
count = 0
# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
    #print(frames.type);
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
     
 
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    #print(cars)
    print(" ")
    for (x,y,w,h) in cars:
        if(x < left and x + w > right):
            count += 1
        if(x > left and x < half and x + w >= right):
            count += 1
    # To draw a rectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
 
   # Display frames in a window 
	cv2.imshow('video2', frames)

    print(count)

    if count > 0:
        print "Done"
        time.sleep(1)
        count = 0
     
   # time.sleep(1)

    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break
 
# De-allocate any associated memory usage
cv2.destroyAllWindows()
