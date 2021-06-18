import face_recognition
face_1 = face_recognition.load_image_file("training_img/fadel.jpeg")
face_1_encoding = face_recognition.face_encodings(face_1)[0]
face_2 = face_recognition.load_image_file("training_img/daffa.jpg")
face_2_encoding = face_recognition.face_encodings(face_2)[0]
known_face_encodings = [
face_1_encoding,
face_2_encoding,
]
known_face_names =  ['fadel.jpeg', 'daffa.jpg']
