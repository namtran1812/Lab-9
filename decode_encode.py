def encode(password):
    encoded_string = ""
    for digit in str(password):
        add_three = str(int(digit) + 3)
        encoded_string += add_three
    return encoded_string

def decode(encoded_string):
    decoded_string = ''
    count = ''
    for char in encoded_string:
        if char.isdigit():
            count += char
        else:
            decoded_string += char * int(count)
            count = ''
    return decoded_string


def main():
    while True:
        menu()
        option = int(input("\nPlease enter an option: "))
        if option == 1:
            password = int(input("Please enter your password to encode: "))
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            original = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {original}.")
        elif option == 3:
            break
def menu():
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    return

if __name__ == '__main__':
    main()