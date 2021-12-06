import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate kunci publik and kunci private

publickey = key.publickey() #ekspor kunci publik untuk di-exchange

# Enkripsi
encryptor = PKCS1_OAEP.new(publickey) #gunakan instansi dari PKCS1_OAEP
encrypted = encryptor.encrypt(b'Tanzil Rahmatul Karim') #pesan untuk dienkripsi

print('Hasil Enkripsi:', encrypted)

# Menambahkan teks pada file .txt
f = open ('enkripsi-new.txt', 'a') #append file
f.write('File telah memiliki content!') #tambahkan isi teks alert ini ke file enkripsi-new.txt
f.close()

# Update file .txt
f = open ('enkripsi-update.txt', 'w') #buka file txt, 'w' adalah write
f.write('Isi file hasil enkripsi telah diupdate!') #teks alert untuk menampilkan update dari file enkripsi-new.txt, namun disini saya sengaja membuat file lagi (enkripsi-update.txt) supaya bisa dibedakan
f.write(str(encrypted)) #menambahkan hasil enkripsi di samping teks alert
f.close()

f = open('enkripsi-update.txt', 'r') #'r' adalah read
message = f.read()

# Dekripsi
decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))

print('Hasil Dekripsi:', decrypted)

f = open ('dekripsi.txt', 'w')
f.write('Isi file hasil dekripsi:') #tambahkan isi teks ini ke file dekripsi.txt
f.write(str(decrypted)) #hasil dekripsi akan ditampilkan di samping teks line 39
f.close()
