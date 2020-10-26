def xor_crypt_string(data, key = 'awesomepassword', encode = False, decode = False):
    from itertools import zip, cycle
    import base64
    
    if decode:
        data = base64.decodestring(data)
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
    
    if encode:
        return base64.encodestring(xored).strip()
    return xored

secret_data = "XOR procedure"

print("The cipher text is ", xor_crypt_string(secret_data, encode = True))
print("The plain text fetched ", xor_crypt_string(xor_crypt_string(secret_data, encode = True),decode = True))

