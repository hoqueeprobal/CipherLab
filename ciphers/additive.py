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


def decrypt(ciphertext, key):

    ciphertext = ciphertext.upper()
    plaintext = ""

    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        if 'A' <= ch <= 'Z':
            c = ord(ch) - ord('A')
            p = (c - key) % 26
            plaintext += chr(p + ord('A'))
        else:
            plaintext += ch

    print("\n===== ADDITIVE CIPHER DECRYPTION =====")
    print("Ciphertext:", ciphertext)
    print("Plaintext :", plaintext)