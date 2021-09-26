import string

# ! The cide below will store the alphabet.
# "abcdefghijklmnopqrstuvwxyz"
alphabet = string.ascii_lowercase


def decrypt(encrypted_message, key):
    encrypted_message = encrypted_message.lower()
    decrypted_message = ""

    for c in encrypted_message:
        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print(decrypted_message)


decrypt("FTQ CGUOW NDAIZ RAJ VGYBE AHQD FTQ XMLK PAS AR OMQEMD MZP KAGD GZUCGQ EAXGFUAZ UE PUMOADYNSUTS", 12)
