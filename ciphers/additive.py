def encrypt(plaintext, key):

    plaintext = plaintext.upper()
    ciphertext = ""

    for i in range(len(plaintext)):
        ch = plaintext[i]
        if 'A' <= ch <= 'Z':
            p = ord(ch) - ord('A')
            c = (p + key) % 26
            ciphertext += chr(c + ord('A'))
        else:
            ciphertext += ch

    print("\n===== ADDITIVE CIPHER ENCRYPTION =====")
    print("Plaintext :", plaintext)
    print("Ciphertext:", ciphertext)