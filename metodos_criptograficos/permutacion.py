def permutacion_cifrar(plaintext, key):
    # Convert key from string to list of integers
    key = [int(k) for k in key.split(',')]
    
    # Calculate the length of the key
    key_length = len(key)
    
    # Pad the plaintext to make its length a multiple of the key length
    padding_length = (key_length - (len(plaintext) % key_length)) % key_length
    padded_plaintext = plaintext + ' ' * padding_length
    
    # Initialize the ciphertext
    ciphertext = ''
    
    # Encrypt the plaintext by permuting the characters based on the key
    for i in range(0, len(padded_plaintext), key_length):
        block = padded_plaintext[i:i+key_length]
        permuted_block = ''.join(block[key[j]-1] for j in range(key_length))
        ciphertext += permuted_block
    
    # Remove spaces from the ciphertext
    ciphertext = ciphertext.replace(' ', '')
    
    return ciphertext


def permutacion_descifrar(ciphertext, key):
    # Convert key from string to list of integers
    key = [int(k) for k in key.split(',')]
    
    # Calculate the length of the key
    key_length = len(key)
    
    # Create a list to store the inverse key
    inverse_key = [0] * key_length
    
    # Calculate the inverse key
    for i, k in enumerate(key):
        inverse_key[k-1] = i
    
    # Initialize the plaintext
    plaintext = ''
    
    # Decrypt the ciphertext by permuting the characters based on the inverse key
    for i in range(0, len(ciphertext), key_length):
        block = ciphertext[i:i+key_length]
        if len(block) < key_length:
            block = block.ljust(key_length)
        unpermuted_block = ''.join(block[inverse_key[j]] for j in range(key_length))
        plaintext += unpermuted_block
    
    # Remove spaces from the plaintext
    plaintext = plaintext.replace(' ', '')
    
    return plaintext