def vigenere_cipher(message, key):
    message_modified = message.upper()
    key_modified = key.upper()
    key_extension = key_modified * ((len(message_modified)//len(key_modified)) + key_modified[:len(message_modified) % len(key_modified)])
    FV = ""
    for i in range(len(message_modified)):
        if message_modified[i] == " ":
            FV += " "
        else:
            base = ord("A")
            shifted_ascii = (ord(message_modified[i]) - base + (ord(key_extension[i]) - base))
            shifted_letter = chr(shifted_ascii + base)
            FV += shifted_letter
    return FV