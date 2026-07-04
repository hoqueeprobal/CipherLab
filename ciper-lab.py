from ciphers.additive import encrypt


def main():

    print("      Ciper Lab")

    print("1. Additive Cipher")
    print("0. Exit")

    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:
        plaintext = input("Enter Plaintext: ")
        key = int(input("Enter Key: "))
        encrypt(plaintext, key)

    elif choice == 0:
        print("Thank You!")
    else:
        print("Invalid Choice!")

main()