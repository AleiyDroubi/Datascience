def vigenere_encryption(plaintext, keyword):
    keyword = keyword.lower()
    result = ""
    keyword_index = 0

    for char in plaintext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shift = ord(keyword[keyword_index]) - 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += encrypted_char
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            result += char
    return result

def vigenere_decryption(ciphertext, keyword):
    keyword = keyword.lower()
    result = ""
    keyword_index = 0

    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord("A") if char.isupper() else ord("a")
            shift = ord(keyword[keyword_index]) - 97
            decrypted_char = chr((ord(char) - ascii_offset - shift + 26) % 26 + ascii_offset)
            result += decrypted_char
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            result += char
    return result


ciphertext = input("citext ")
keyword = input("keyword ")

dycrpted = vigenere_decryption(ciphertext, keyword)

print(dycrpted)