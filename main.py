#Author : Aymane ISSAMI
#----------------------------------------------------------------------------------------------------------------

print("Enter a Number :")
choice = input(" 1.Generate a Key:\n 2.Encrypt:\n 3.Decrypt: ").strip()

if  choice == "1"  :
    from cryptography.fernet import Fernet

    #Getting the Key
    key = Fernet.generate_key()
    print(key)

    #Saving the key
    file = open('key.key', 'wb')  
    file.write(key)
    file.close()

elif choice == "2"  :
    from cryptography.fernet import Fernet

    key = b'' #Enter your secret key between ''
    input_file = 'password.txt'
    output_file = 'password.encrypted'

    with open(input_file, 'rb') as f:
        data = f.read()
        print("Your password is :")
        print(data)  

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)
        print("Your password.encrypted is :")
        print(encrypted)

elif choice == "3"  :
    from cryptography.fernet import Fernet, InvalidToken

    key = b'' #Enter your secret key between ''
    input_file = 'password.encrypted'
    output_file = 'password.txt'

    with open(input_file, 'rb') as f:
        data = f.read()
        print("Your password.encrypted is :")
        print(data)

    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(data)

        with open(output_file, 'wb') as f:
            f.write(decrypted)
            print("Your password is :")
            print(decrypted) 

    except InvalidToken as e:
        print("Invalid Key - Unsuccessfully decrypted")

else:
    print("\n invalid choice, Please try again")

