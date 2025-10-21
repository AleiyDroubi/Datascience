def columnar_encrypt(plaintext, key):
    """
    Encrypt plaintext using Columnar Transposition Cipher
    """
    # Remove spaces and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()
    
    # Calculate number of rows needed
    num_cols = len(key)
    num_rows = (len(plaintext) + num_cols - 1) // num_cols  # Ceiling division
    
    # Pad plaintext if necessary
    padded_text = plaintext.ljust(num_rows * num_cols, 'X')
    
    # Create grid
    grid = []
    for i in range(num_rows):
        start = i * num_cols
        end = start + num_cols
        grid.append(list(padded_text[start:end]))
    
    # Get column order based on sorted key
    key_order = sorted([(char, idx) for idx, char in enumerate(key)])
    column_order = [idx for char, idx in key_order]
    
    # Read columns in key order
    ciphertext = ""
    for col_idx in column_order:
        for row in range(num_rows):
            ciphertext += grid[row][col_idx]
    
    return ciphertext

def columnar_decrypt(ciphertext, key):
    """
    Decrypt ciphertext using Columnar Transposition Cipher
    """
    key = key.upper()
    num_cols = len(key)
    num_rows = (len(ciphertext) + num_cols - 1) // num_cols  # Ceiling division
    
    # Create empty grid  with columns X rows 
    grid = [[''] * num_cols for _ in range(num_rows)]
    
    # Get column order based on sorted key 
    """ Key: K E Y
Index: 0 1 2

Sort key alphabetically: E(1), K(0), Y(2)
Column order: [1, 0, 2] """
    key_order = sorted([(char, idx) for idx, char in enumerate(key)])
    column_order = [idx for char, idx in key_order]
    
    # Fill the grid column-wise
    index = 0
    for col_idx in column_order:
        for row in range(num_rows):
            if index < len(ciphertext):
                grid[row][col_idx] = ciphertext[index]
                index += 1
    
    # Read the grid row-wise to get plaintext
    plaintext = ""
    for row in range(num_rows):
        plaintext += ''.join(grid[row])
    
    return plaintext.rstrip('X')  # Remove padding if any



# Example usage
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")
encrypted = columnar_encrypt(plaintext, key)
print("Encrypted text:", encrypted)

 # Decrypt
decrypted = columnar_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
    
# Demonstration
print("\n" + "=" * 30)
print("DEMONSTRATION:")
print(f"Original:  {plaintext}")
print(f"Key:       {key}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
print(columnar_decrypt("ILEDTN HPTRSO LITMAX SAXERXTANONI SNFOTX", "SECRET"))  # Example decryption 