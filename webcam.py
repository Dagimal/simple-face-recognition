"""
SIMPLE FACE RECOGNITION SYSTEM [PENGENALAN NAMA PADA WAJAH]
Original Author : ageitgey
Author          : Daffa Gifari Akmal,
                  Fadel Januar A.
Date            : 7-June-2021
Version         : 1.0
-----------------------------------------------------------
Adalah sistem sederhana untuk melakukan pengenalan nama pada wajah dengan cara
mencocokkan wajah pada foto sampel yang kita berikan.
"""

import face_recognition
from training_data_contoh import *
import cv2
import numpy as np

# ambil gambar di webcam
video_capture = cv2.VideoCapture(0)

# load sampel gambar dan mencocokkan
#obama_image = face_recognition.load_image_file("training_img/fadel.jpeg")
#obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

#biden_image = face_recognition.load_image_file("training_img/daffa.jpg")
#biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# membuat list nama wajah sesuai dengan gambar sampel diatas
#known_face_encodings = [
#    obama_face_encoding,
#    biden_face_encoding
#]
#known_face_names = [
#    "Fadel Januar A.",
#    "Daffa Gifari Akmal"
#]

while True:
    # Mengambil tiap frame dari video
    ret, frame = video_capture.read()

    # Convert gambar dari BGR color (OpenCV) ke RGB (face_recognition)
    rgb_frame = frame[:, :, ::-1]

    # Mencari semua encoding wajah dalam frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name.replace(".jpg",""), (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Menampilkan hasil gambar
    cv2.imshow('Video', frame)

    # shortcut untuk exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Exit window
video_capture.release()
cv2.destroyAllWindows()

