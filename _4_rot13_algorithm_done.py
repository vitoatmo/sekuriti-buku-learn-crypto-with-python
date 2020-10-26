#ROT13 cipher refers to the abbreviated form Rotate by 13 places.
print("\n<< BISA - ROT13 >>\n")

# Function to translate plain text
def rot13(text):
    #ROT13 cipher refers to the abbreviated form Rotate by 13 places.
    rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    return text.translate(rot13trans)

def main():
    txt = input('Input (str): ')
    print('Output 1st: ' + rot13(txt))
    print('Output 2nd: ' + rot13(rot13(txt)))

if __name__ == "__main__":
        main()
