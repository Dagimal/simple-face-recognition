import face_recognition
import numpy as np
from PIL import Image, ImageDraw
from training_data import *
import cv2
import os
import easygui

def banner():
	print(
		"""
  ___            _ _          
 | __|_ _ __ ___| _ \___ __ _ 
 | _/ _` / _/ -_)   / -_) _` |
 |_|\__,_\__\___|_|_\___\__, |
  Created By:           |___/ v1.0
  Daffa Gifari Akmal
  Fadel Januar Alfiansyah
		"""
	)

def photoFaceRecognition():
	try:
		file_name = easygui.fileopenbox()
		unknown_image = face_recognition.load_image_file(file_name)
		unknown_image_to_draw = cv2.imread(file_name)
	
		face_locations = face_recognition.face_locations(unknown_image)
		face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
	
		pil_image = Image.fromarray(unknown_image)
		draw = ImageDraw.Draw(pil_image)
	
		for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
			# Mencocokkan_Foto
			matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
	
			name = "Unknown"
	
			face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
			best_match_index = np.argmin(face_distances)
			if matches[best_match_index]:
				name = known_face_names[best_match_index]
	
			# Membuat_Box
			cv2.rectangle(unknown_image_to_draw,(left, top), (right, bottom), (0,255,0),3 )
			draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 255))
			cv2.putText(unknown_image_to_draw,name,(left,top-20), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 2,cv2.LINE_AA)
			print("===>> ",name)
		frame = "Wajah Terdeteksi : " + name
		cv2.imshow(frame, unknown_image_to_draw)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	except Exception as e:
		print(e)

def liveCamera():
	os.system("python webcam.py")

def trainingData():
	os.system("python training.py")

def mainMenu():
	print("[0] TRAINING DATA")
	print("[1] PHOTO RECOGNITION")
	print("[2] LIVE RECOGNITION")

banner()
mainMenu()

choice = input(">> ")

if choice == "1":
	photoFaceRecognition()
elif choice == "2":
	liveCamera()
elif choice == "0":
	trainingData()
else:
	print("INPUTAN SALAH!!!")
	exit()
