# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 21:47:35 2018

@author: Vinayaki
"""

import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
 
def encrypt(key, filename):
    chunk_size = 64*1024
    output_file = "enc_" + filename
    file_size = str(os.path.getsize(filename)).zfill(16)
    IV = os.urandom(16)
    print(len(IV))
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    with open(filename, 'rb') as inputfile:
        with open(output_file, 'wb') as outf:
            outf.write(file_size.encode(encoding='utf-8'))
            outf.write(IV)
            while True:
                chunk = inputfile.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                   chunk += (' '*(16 - len(chunk)%16)).encode(encoding='utf-8')
                outf.write(encryptor.encrypt(chunk))
 
def decrypt(key, filename):
        chunk_size = 64*1024
        output_file = "dec_" + filename[4:]
        with open(filename, 'rb') as inf:
            filesize = int(inf.read(16).decode(encoding='utf-8'))
            IV = inf.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, IV)
            with open(output_file, 'wb') as outf:
                while True:
                    chunk = inf.read(chunk_size)
                    if len(chunk)==0:
                        break
                    outf.write(decryptor.decrypt(chunk))
                outf.truncate(filesize)
 
def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()
 
def main():
    choice = input("Select One of the following\n> 1. Encrypt \n> 2. Decrypt\n>>> ")
    if choice == "1":
        filename = input("Enter the name of file to be encrypted >> ")
        password = input("Enter the password")
        encrypt(getKey(password), filename)
        print("Done!\n%s ==> %s"%(filename, "enc_" + filename))
    elif choice == "2":
        filename = input("File to be decrypted > ")
        password = input("Password: ")
        decrypt(getKey(password), filename)
        print("Done\n%s ==> %s"%(filename, "dec_" + filename[4:]))
    else:
        print("No option Selected")
 
if __name__ == "__main__":
    main()