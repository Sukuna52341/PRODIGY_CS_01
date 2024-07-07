
def caesar_cipher(text, key, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key if mode == 'e' else -key
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print()
print('CAESAR CIPHER PROGRAM')
print()

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()

if user_input == 'e':
    print()
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 - 26): '))
    text = input('Enter the text to encrypt: ')
    encrypted_text = caesar_cipher(text, key, 'e')
    print('Encrypted text:', encrypted_text)

elif user_input == 'd':
    print()
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 - 26): '))
    text = input('Enter the text to decrypt: ')
    decrypted_text = caesar_cipher(text, key, 'd')
    print('Decrypted text:', decrypted_text)