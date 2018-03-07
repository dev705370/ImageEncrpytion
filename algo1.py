# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 20:14:20 2018

@author: Vinayaki
"""
from scipy import misc

ENCRYPT = 'encrypt'
DECRYPT = 'decrypt'

def encrypt(imageToEncryptPath, keyImagePath):
    imageToEncrypt = misc.imread(imageToEncryptPath)
    keyImage = misc.imread(keyImagePath)
    
    keyImage.resize(imageToEncrypt.shape)
    encryptedImage = imageToEncrypt ^ keyImage
    return encryptedImage
    
def decrypt(imageTodecryptPath, keyImagePath):
    imageTodecrypt = misc.imread(imageTodecryptPath)
    keyImage = misc.imread(keyImagePath)
    
    keyImage.resize(imageTodecrypt.shape)
    decryptedImage = imageTodecrypt ^ keyImage
    return decryptedImage


def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

if __name__ == '__main__':
    import sys
    from sys import argv
    #myargs = getopts(argv)
    #myargs = {'-i': 'input.jpeg', '-key': 'key.jpeg', '-algo': ENCRYPT, '-o': 'out.jpeg' }
    myargs = {'-i': 'out.jpeg', '-key': 'key.jpeg', '-algo': DECRYPT, '-o': 'out1.jpeg' }
    if '-i' not in myargs:
        print("pass input image as -i")
        sys.exit(1)
    if '-key' not in myargs:
        print("pass key image as -key")
        sys.exit(1)
    if '-algo' not in myargs:
        print("pass decrpty/encrypt options as -algo")
        sys.exit(1)
    if myargs['-algo'] != ENCRYPT and myargs['-algo'] != DECRYPT:
        print("Only allowed values for -algo are " + ENCRYPT + "/" + DECRYPT)
        sys.exit(1)
    if '-o' not in myargs:
        print("pass output location as -o")
        sys.exit(1)
        
    outImage = [];
    if myargs['-algo'] == ENCRYPT:
        outImage = encrypt(myargs['-i'], myargs['-key'])
    else:
        outImage = decrypt(myargs['-i'], myargs['-key'])
     
    misc.imsave(myargs['-o'], outImage)
    