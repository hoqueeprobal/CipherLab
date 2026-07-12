def encrypt(plaintext, key):

    plaintext = plaintext.upper()
    ciphertext = ""

    if key <= 0 or key >= 26:
        print("Invalid Key!")
        return

    if key not in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        print("Invalid Key! Key must be coprime with 26.")
        return

    for i in range(len(plaintext)):
        ch = plaintext[i]
        if 'A' <= ch <= 'Z':
            p = ord(ch) - ord('A')
            c = (p * key) % 26
            cipher_char = chr(c + ord('A'))
            ciphertext += cipher_char

        else:
            ciphertext += ch

    print("\n===== MULTIPLICATIVE CIPHER ENCRYPTION =====")
    print("Plaintext :", plaintext)
    print("Ciphertext:", ciphertext)