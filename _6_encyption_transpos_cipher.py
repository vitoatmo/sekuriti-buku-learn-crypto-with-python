import pyperclip

print("\n<< BISA - ENCRYPTION TRANSPOSITION CIPHER >>\n")

def main():
    myMessage = input("Input : ")
    myKey = int(input("Key : "))
    ciphertext = encryptMessage(myKey, myMessage)
    print("\nCipher Text is")
    print('>> ' + ciphertext)
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    ciphertext = [''] * key
    
    for col in range(key):
        position = col

        while position < len(message):
            ciphertext[col] += message[position]
            position += key
    return ''.join(ciphertext)  # Cipher text

if __name__ == '__main__':
    main()
