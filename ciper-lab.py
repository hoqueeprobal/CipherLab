from ciphers.additive import encrypt as additive_encrypt
from ciphers.multiplicative import encrypt as multiplicative_encrypt


def main():

    print("      Cipher Lab\n")
    print("1. Additive Cipher")
    print("2. Multiplicative Cipher")
    print("0. Exit")

    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:

        plaintext = input("Enter Plaintext: ")
        key = int(input("Enter Key: "))
        additive_encrypt(plaintext, key)

    elif choice == 2:

        plaintext = input("Enter Plaintext: ")
        key = int(input("Enter Key: "))
        multiplicative_encrypt(plaintext, key)

    elif choice == 0:
        print("Thank You!")

    else:
        print("Invalid Choice!")


main()