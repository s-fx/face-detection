import cv2

face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
isPressed = False

# VideoCapture Object
capture = cv2.VideoCapture(0)

print("--------------------------------------")
print("Start Video Capture, press 'q' to quit")
print("Press CTRL + p to see buttons to start Face Detection")

def isActive(*args):
	global isPressed
	isPressed = True
	pass

def isNotActive(*args):
	global isPressed
	isPressed = False
	pass


cv2.namedWindow("Face Detection")
# you have to press ctrl+p to show the button inside the frame
cv2.createButton("Face Detection Start", isActive, None, cv2.QT_PUSH_BUTTON, 1)
cv2.createButton("Face Detection Stop", isNotActive, None, cv2.QT_PUSH_BUTTON, 1)


while True:
	ret, frame = capture.read()
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	
	faces = face_cascade.detectMultiScale(frame_gray, 1.25, 4)

	if isPressed:
		# draw box
		for (x,y,h,w) in faces:
			cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,0), 2)
			rec_color = frame[y:y+h, x:x+w]

	# show frame with box
	cv2.imshow("Face Detection", frame)
	
	# quit with q
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break




# clean up
capture.release()
cv2.destroyAllWindows()
