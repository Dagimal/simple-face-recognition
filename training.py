#import face_recognition
from tqdm import tqdm
import os

openFile = "training_data_contoh.py"

def training():
	os.remove(openFile)
	list_dir = os.listdir("training_img")
	loop = -1
	pbar = tqdm(total = len(list_dir))
	f = open(openFile, "a")
	print("import face_recognition", file=f)
	while loop <= len(list_dir):
		try:
			loop += 1
			print("SEDANG MEMBUAT TRAINING DATA ...")

			## menulis untuk training_data.py menggunakan for, membaca dari folder training_img
			#f = open("training_data_contoh.py", "w")
			#print("import face_recognition", file=f)
			print('face_'+str(loop+1) + ' = face_recognition.load_image_file("training_img/'+ list_dir[loop] + '")', file=f)
			print('face_'+str(loop+1)+'_encoding = face_recognition.face_encodings(face_' + str(loop+1) + ')[0]', file=f)
			#face_1 = face_recognition.load_image_file("training_img/fadel.jpeg")
			#face_1_encoding = face_recognition.face_encodings(face_1)[0]

			#face_2 = face_recognition.load_image_file("training_img/daffa.jpg")
			#face_2_encoding = face_recognition.face_encodings(face_2)[0]
			#known_face_encodings = [face_1_encoding,face_2_encoding]

			#known_face_names = ["fadel","daffa"]
			pbar.update(1)
		except:
			print("looping nya error mas")
	# Knows Face Encodings
	print("known_face_encodings = [", file=f)
	tambah = 0
	for i in range(len(list_dir)):
		tambah += 1
		print("face_"+str(tambah)+"_encoding,", file=f)
	print("]", file=f)
	
	# Known Face Names
	print("known_face_names = ", list_dir, file=f)
	#print(",".join(list_dir), file=f)
	#print("]", file=f)
print("++ PASTIKAN NAMA FILE SUDAH SESUAI DENGAN NAMA ORANG ++")

print("Lanjut? [y/N]")
choice = input(">> ")

if choice == "y" or choice == "Y":
	training()
	print("training data sudah berhasil di build!")
elif choice == "n" or choice == "N":
	exit()
