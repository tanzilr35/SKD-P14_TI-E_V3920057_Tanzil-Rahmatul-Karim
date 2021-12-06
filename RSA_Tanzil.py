import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate kunci publik and kunci private

publickey = key.publickey() #ekspor kunci publik untuk di-exchange

# Enkripsi
encryptor = PKCS1_OAEP.new(publickey) #gunakan instansi PKCS1_OAEP
encrypted = encryptor.encrypt(b'Tanzil Rahmatul Karim') #pesan untuk enkripsi

print('Hasil Enkripsi:', encrypted) #ciphertext

# Menambahkan teks pada file .txt
f = open ('enkripsi-new.txt', 'a') 
f.write('File telah memiliki content!') #tulis ciphertext ke file
f.close()

# Update file .txt
f = open ('enkripsi-update.txt', 'w') #buka file txt, 'w' adalah write
f.write('Isi file hasil enkripsi telah diupdate!')
f.write(str(encrypted))
f.close()

f = open('enkripsi-update.txt', 'r') #'r' adalah read
message = f.read()

# Dekripsi
decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))

print('Hasil Dekripsi:', decrypted)

f = open ('dekripsi.txt', 'w')
f.write('Isi file hasil dekripsi:')
f.write(str(decrypted))
f.close()