def caeser_cipher_encyption(text,shift):
    reult=""
    for char in text:
        shifted = (ord(char) + shift) % 256
        reult += chr(shifted)
    return reult


def caeser_cipher_encyption2_0(text,shift):
    reult=""

    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_offset + shift) % 26 # Wrap around the alphabet
            reult += chr(shifted + ascii_offset)
        else:
            reult += char  # Non-alphabetic characters are added unchanged
    return reult




text = input("Enter the text to be encrypted: ")
shift = int(input("Enter the shift value (1-255): "))
if shift < 1 or shift > 255:
    print("Shift value must be between 1 and 255.")
else:
    encrypted_text = caeser_cipher_encyption(text, shift)
    print("Encrypted text:", encrypted_text)