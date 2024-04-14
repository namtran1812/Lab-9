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
        print('Menu')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        choice = int(input('Please enter an option: '))
        if choice == 3:
            break
        else:
            password = input('Please enter your password to encode: ')
            if choice == 1:
                encode = encode(password)
                print('Your password has been encoded and stored!')
            elif choice == 2:
                print(f'The encoded password is {encode}, and the original password is {password}.')

if __name__ == '__main__':
    main()