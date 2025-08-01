def caesar_cipher_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                encrypted += chr((shifted - ord('a')) % 26 + ord('a'))
            else:
                encrypted += chr((shifted - ord('A')) % 26 + ord('A'))
        else:
            encrypted += char  # leave spaces/punctuation untouched
    return encrypted

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # just reverse the shift

def main():
    print("Welcome to your own personal Caesar Cipher Encrypt/Decrypt Tool")
    choice = input("Type 'encrypt' to encode, 'decrypt' to decode: ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value"))

    if choice == "encrypt":
        result = caesar_cipher_encrypt(message, shift)
        print(f" Encrypted message: {result}")
    elif choice == "decrypt":
        result = caesar_cipher_decrypt(message, shift)
        print(f" Decrypted message: {result}")
    else:
        print(" Invalid choice. Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()