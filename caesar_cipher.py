def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        shift = -shift  # reverse the shift for decryption

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - start + shift) % 26
            result += chr(start + offset)
        else:
            result += char  # non-alphabetic characters remain unchanged
    return result

# Main program
def main():
    print("=== Caesar Cipher ===")
    mode = input("Enter mode (encrypt/decrypt): ").lower()
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Shift value must be an integer.")
        return

    output = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode}ed): {output}")

if __name__ == "__main__":
    main()
