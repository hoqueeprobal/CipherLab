from ciphers.additive import encrypt as additive_encrypt
from ciphers.additive import decrypt as additive_decrypt
from ciphers.multiplicative import encrypt as multiplicative_encrypt
from ciphers.affine import encrypt as affine_encrypt
from ciphers.affine import decrypt as affine_decrypt


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

        text = input("Enter Text: ")
        key = int(input("Enter Key: "))
        multiplicative_encrypt(text, key)

    elif choice == 3:

        print("\n1. Encrypt")
        print("2. Decrypt")

        operation = int(input("Enter Choice: "))

        text = input("Enter Text: ")
        a = int(input("Enter Key 'a': "))
        b = int(input("Enter Key 'b': "))

        if operation == 1:
            affine_encrypt(text, a, b)

        elif operation == 2:
            affine_decrypt(text, a, b)

        else:
            print("Invalid Choice!")

    elif choice == 0:

        print("Thank You!")

    else:

        print("Invalid Choice!")


main()