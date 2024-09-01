def caesar_cipher(text, shift, action):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                start = ord('a') 
            else:
                start = ord('A')

            if action == 'e':
                shift_direction = shift 
            else:
                shift_direction = -shift
            result += chr((ord(char) - start + shift_direction) % 26 + start)
        else:
            result += char
    return result

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    action = input("Select E or D for Encryption and Decryption: ").lower()
    while action not in ['e', 'd']:
        print("Please choose e or d")
        action = input("Select E or D for Encryption and Decryption: ").lower()
    result = caesar_cipher(message, shift, action)
    print(f"Message: {result}")

if __name__ == "__main__":
    main()