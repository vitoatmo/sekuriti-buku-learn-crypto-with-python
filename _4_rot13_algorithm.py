#ROT13 cipher refers to the abbreviated form Rotate by 13 places.

def rot13(phrase):
   abc = "abcdefghijklmnopqrstuvwxyz"
   out_phrase = ""
   for char in phrase:
       out_phrase += abc[(abc.find(char)+13) % 26]
   return out_phrase

phrase = input("Masukan input : ")
print("Hasil ROT13 1st: ", rot13(phrase))
# kgurkehffvnafknerkpbzvat
print("Hasil ROT13 2nd : ", rot13(rot13(phrase)))
# What's the output?


# ##BELOM BISA
# #ROT13 cipher refers to the abbreviated form Rotate by 13 places.
# rot13trans = string.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#           'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

# # Function to translate plain text
# def rot13(text):
#     return text.translate(rot13trans)

# def main():
#     txt = "ROT13 Algorithm"
#     print(rot13(txt))

# if __name__ == "__main__":
#         main()
