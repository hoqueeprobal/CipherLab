from ciphers.additive import encrypt as additive_encrypt
from ciphers.additive import decrypt as additive_decrypt
from ciphers.multiplicative import encrypt as multiplicative_encrypt
from ciphers.affine import encrypt as affine_encrypt


def main():

    print("      Cipher Lab\n")
    print("1. Additive Cipher")
    print("2. Multiplicative Cipher")
    print("3. Affine Cipher")
    print("0. Exit")

    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:

        print("\n1. Encrypt")
        print("2. Decrypt")
        operation = int(input("Enter Choice: "))

        text = input("Enter Text: ")
        key = int(input("Enter Key: "))

        if operation == 1:
            additive_encrypt(text, key)
        elif operation == 2:
            additive_decrypt(text, key)
        else:
            print("Invalid Choice!")

    elif choice == 2:
        plaintext = input("Enter Plaintext: ")
        key = int(input("Enter Key: "))
        multiplicative_encrypt(plaintext, key)

    elif choice == 3:
        plaintext = input("Enter Plaintext: ")
        a = int(input("Enter Key 'a': "))
        b = int(input("Enter Key 'b': "))
        affine_encrypt(plaintext, a, b)

    elif choice == 0:
        print("Thank You!")

    else:
        print("Invalid Choice!")


main()