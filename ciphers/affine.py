def encrypt(plaintext, a, b):

    plaintext = plaintext.upper()
    ciphertext = ""

    if a not in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        print("Invalid Key! 'a' must be coprime with 26.")
        return

    for i in range(len(plaintext)):

        ch = plaintext[i]

        if 'A' <= ch <= 'Z':

            p = ord(ch) - ord('A')
            c = (a * p + b) % 26

            ciphertext += chr(c + ord('A'))

        else:

            ciphertext += ch

    print("\n===== AFFINE CIPHER ENCRYPTION =====")
    print("Plaintext :", plaintext)
    print("Ciphertext:", ciphertext)


def decrypt(ciphertext, a, b):

    ciphertext = ciphertext.upper()
    plaintext = ""

    # Valid values of a
    if a not in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        print("Invalid Key! 'a' must be coprime with 26.")
        return

    # Multiplicative inverse of a (mod 26)
    inverse = {
        1: 1,
        3: 9,
        5: 21,
        7: 15,
        9: 3,
        11: 19,
        15: 7,
        17: 23,
        19: 11,
        21: 5,
        23: 17,
        25: 25
    }

    a_inverse = inverse[a]

    for i in range(len(ciphertext)):

        ch = ciphertext[i]

        if 'A' <= ch <= 'Z':

            c = ord(ch) - ord('A')
            p = (a_inverse * (c - b)) % 26

            plaintext += chr(p + ord('A'))

        else:

            plaintext += ch

    print("\n===== AFFINE CIPHER DECRYPTION =====")
    print("Ciphertext:", ciphertext)
    print("Plaintext :", plaintext)