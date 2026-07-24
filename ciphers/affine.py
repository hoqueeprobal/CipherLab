def encrypt(plaintext, a, b):

    plaintext = plaintext.upper()
    ciphertext = ""

    # a must be coprime with 26
    if a not in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        print("Invalid Key! 'a' must be coprime with 26.")
        return

    for i in range(len(plaintext)):

        ch = plaintext[i]

        if 'A' <= ch <= 'Z':

            p = ord(ch) - ord('A')
            c = (a * p + b) % 26

            cipher_char = chr(c + ord('A'))
            ciphertext += cipher_char

        else:

            ciphertext += ch

    print("\n===== AFFINE CIPHER ENCRYPTION =====")
    print("Plaintext :", plaintext)
    print("Ciphertext:", ciphertext)