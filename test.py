import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

def applyblur(image,factor=3.0):
	(h, w) = image.shape[:2]
	kW = int(w / factor)
	kH = int(h / factor)
	
	if kW % 2 == 0:
		kW -= 1
	
	if kH % 2 == 0:
		kH -= 1
	return cv2.GaussianBlur(image, (kW, kH), 0)

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


def detect_faces(frame):
	gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray_image, 1.1, 4)

	return faces

def main():
	while True:
		
		frame = cap.read()[1]
		scale_percent = 80 # percent of original size
		width = int(frame.shape[1] * scale_percent / 100)
		height = int(frame.shape[0] * scale_percent / 100)
		dim = (width, height)


		frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
      
		faces = detect_faces(frame)

		for x in range(len(faces)):
			(x,y,w,h) = faces[x]
			#frame[y:y+h, x:x+w] = applyblur(frame[y:y+h, x:x+w])
			frame[y:y+h, x:x+w] = applyblur_pixelate(frame[y:y+h, x:x+w])

		cv2.imshow("Face Mask Detector - BETA Jetson Nano", frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

main()