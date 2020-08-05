#importing the necessary libraries
import cv2
import numpy as np
import sys

#creating the OpenCV webcam object and Loading the face detection Haar Cascade
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

#Function to apply gaussian blur
def applyblur(image,factor=3.0):
	(h, w) = image.shape[:2]
	kW = int(w / factor)
	kH = int(h / factor)
	
	if kW % 2 == 0:
		kW -= 1
	
	if kH % 2 == 0:
		kH -= 1
	return cv2.GaussianBlur(image, (kW, kH), 0)

#function to apply pixelated blur
def applyblur_pixelate(image,blocks=10):
	(h, w) = image.shape[:2]
	xSteps = np.linspace(0, w, blocks + 1, dtype="int")
	ySteps = np.linspace(0, h, blocks + 1, dtype="int")
	
	for i in range(1, len(ySteps)):
		for j in range(1, len(xSteps)):
			startX = xSteps[j - 1]
			startY = ySteps[i - 1]
			endX = xSteps[j]
			endY = ySteps[i]
			roi = image[startY:endY, startX:endX]
			(B, G, R) = [int(x) for x in cv2.mean(roi)[:3]]
			cv2.rectangle(image, (startX, startY), (endX, endY),
				(B, G, R), -1)

	return image

'''
def detect_faces():
function handles the face detection operation using OpenCV
receives the frame captured as argument
return the co-ordinates of detected face
'''
def detect_faces(frame):
	gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray_image, 1.1, 4)

	return faces

'''
def main():
handles the main while loop and is the driver function
'''

def main():
	#handling the CLA
	try:
		blur_type = sys.argv[1]
		if blur_type!="gaussian" and blur_type!="pixelate":
			print("Possible error with the command Line Argument !!!")
			exit(-1)
	except:
		print("Missing command line argument to determine the type of blur !")
		exit(-1)

	while True:		
		#capturing frame
		frame = cap.read()[1]

		#applying scaling
		scale_percent = 80 # percent of original size
		width = int(frame.shape[1] * scale_percent / 100)
		height = int(frame.shape[0] * scale_percent / 100)
		dim = (width, height)


		frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
      
      	#detecting faces in frame
		faces = detect_faces(frame)

		for x in range(len(faces)):
			(x,y,w,h) = faces[x]
			if blur_type == "gaussian":
				frame[y:y+h, x:x+w] = applyblur(frame[y:y+h, x:x+w])
			else:
				frame[y:y+h, x:x+w] = applyblur_pixelate(frame[y:y+h, x:x+w])

		cv2.imshow("FaceBlur using OpenCV", frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

if __name__ == "__main__":
	main()