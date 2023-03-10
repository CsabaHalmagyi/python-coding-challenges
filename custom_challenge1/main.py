# Custom challenge 1 - Storing a secret message in a file:
# Write a program that has the following Menu:
# 1 - Create a secret message
# 2 - Read a secret message
# 3 - EXIT
#
# 1 - prompts the user for a password and a secret message. Then stores the secret password and the message encoded
# in a file.
#
# 2 - Asks for the password. If the password is correct then displays the secret message from the file.
# If the password is incorrect, ask for it 4 more times, then EXIT.
#
# 3 - Exits.




import zlib
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

def obscure(data: bytes) -> bytes:
    return b64e(zlib.compress(data, 9))


def unobscure(obscured: bytes) -> bytes:
    return zlib.decompress(b64d(obscured))


def create_secret_message():
    print("Create secret message")
    message = input("Enter the message you want to send:")
    message.replace("\n", "")
    password = input("Enter the password needed to read the message:")
    password.replace("\n", "")
    with open("secret_message.txt", "w") as file:
        file.write(obscure(password.encode()).decode())
        file.write('\n')
        file.write(obscure(message.encode()).decode())
        print("Secret message saved to file.")


def read_secret_message():
    file = open('secret_message.txt', 'r')
    lines = file.readlines()
    secret_password = unobscure(lines[0].replace("\n", "").encode()).decode()
    secret_message = unobscure(lines[1].replace("\n", "").encode()).decode()
    correct_password = False
    attempts = 5
    while (correct_password == False):
        password = input("Enter the password needed to read the message(remaining attempts: "+str(attempts)+"):")
        if(password == secret_password):
            print("Correct password.")
            print("Secret message: "+secret_message)
            correct_password = True
        else:
            attempts -= 1
            print("Incorrect password")
        if (attempts == 0):
            print("No more attempts, exiting.")
            exit()


def message_coder_menu():
    exit = False
    while(exit !=True):
        option = input("Select an option (1-Create secret message, 2-Read secret message, 3-EXIT):")
        if option == "1":
            create_secret_message()
        elif option == "2":
            read_secret_message()
        elif option == "3":
            print("Exiting...")
            exit = True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    message_coder_menu()

