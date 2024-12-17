
# Simplified menu focused on AES standard encryption and decryption in CBC mode and the Modified AES with a vigenere cipher only
# The others AES implementations (AES92,AES256) or mode (ECB) appearing in the code were for test and study purpose in order to understand better the AES encryption

import cripto_aes_functions
import helper

str1 = "1. Encrypt file using AES28 in CBC mode\n"
str2 = "2. Decrypt file using AES28 in CBC mode\n"
str3 = "3. Encrypt file using Vigenère-based AES28\n"
str4 = "4. Decrypt file using Vigenère-based AES128\n"
str5 = "5. Exit\n"

while True:
    try:
        choice = int(input(str1 + str2 + str3 + str4 + str5))
    except ValueError:
        print("Not a number")

    if choice == 1:
        print("Generating AES key...")
        key = cripto_aes_functions.randkeygen(16 * 8)
        print("key:", key)
        
        filename = "livro"
        msg = helper.readFile(filename + ".txt")
        IV = cripto_aes_functions.IVGen(16 * 8)
        cipher=cripto_aes_functions.encrypt(msg, key, 16*8, "CBC", IV)
        # If encrypt returns a tuple, unpack it
        if isinstance(cipher, tuple):
            elapsed_time, cipher = cipher  # Extract only the cipher
        helper.saveCipher(filename + "_AES128.txt", cipher)
        print("Cipher saved at file:", filename + ".txt")


    elif choice == 2:
        #filename = "test"
        strcipher = helper.readFile(filename + "_AES128.txt")
        
        # Split and convert to integers
        try:
            tmp_cipher = strcipher.split(",")
            cipher = [int(i) for i in tmp_cipher]
        except ValueError as e:
            print(f"Error in ciphertext format: {e}")
            continue
        
        plain = cripto_aes_functions.decrypt(cipher, key, 16 * 8, "CBC", IV)
        helper.saveFile(filename + "_AES128_plain.txt", plain)
        print("Decrypted file saved as:", filename + "_AES128_plain.txt")

        
    elif choice == 3:
        print("Generating AES key...")
        key = cripto_aes_functions.randkeygen(16 * 8)
        print("key:", key)
        
        filename = "livro"
        msg = helper.readFile(filename + ".txt")
        IV = cripto_aes_functions.IVGen(16 * 8)
        cipher=cripto_aes_functions.encrypt(msg, key, 16*8, "VIGENERE", IV)
        # If encrypt returns a tuple, unpack it
        if isinstance(cipher, tuple):
            elapsed_time, cipher = cipher  # Extract only the cipher
        helper.saveCipher(filename + "_AES128_Vigenere.txt", cipher)
        print("Cipher saved at file:", filename + ".txt")

    elif choice == 4:
        #filename = "test"
        strcipher = helper.readFile(filename + "_AES128_Vigenere.txt")
        
        # Split and convert to integers
        try:
            tmp_cipher = strcipher.split(",")
            cipher = [int(i) for i in tmp_cipher]
        except ValueError as e:
            print(f"Error in ciphertext format: {e}")
            continue

        plain=cripto_aes_functions.decrypt(cipher, key, 16*8, "VIGENERE", IV)
        helper.saveFile(filename + "_AES128_Vigenere_plain.txt", plain)
        print("Decrypted file saved as:", filename + "_AES128_Vigenere_plain.txt")

    elif choice == 5:
        print("Exited.")
        break
    else:
        print("Please enter a valid entry")
