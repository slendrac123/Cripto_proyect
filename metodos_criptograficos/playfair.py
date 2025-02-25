def generate_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = ''.join(sorted(set(key.upper()), key=key.index))
    matrix = [char for char in key if char in alphabet]
    matrix += [char for char in alphabet if char not in matrix]
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row, line in enumerate(matrix):
        if char in line:
            return row, line.index(char)
    return None

def playfair_cifrar(text, key):
    matrix = generate_playfair_matrix(key)
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"
    pairs = [(text[i], text[i+1]) for i in range(0, len(text), 2)]
    
    encrypted = []
    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            encrypted.append(matrix[row1][(col1 + 1) % 5])
            encrypted.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            encrypted.append(matrix[(row1 + 1) % 5][col1])
            encrypted.append(matrix[(row2 + 1) % 5][col2])
        else:
            encrypted.append(matrix[row1][col2])
            encrypted.append(matrix[row2][col1])
    return ''.join(encrypted)

def playfair_descifrar(text, key):
    matrix = generate_playfair_matrix(key)
    pairs = [(text[i], text[i+1]) for i in range(0, len(text), 2)]
    
    decrypted = []
    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            decrypted.append(matrix[row1][(col1 - 1) % 5])
            decrypted.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            decrypted.append(matrix[(row1 - 1) % 5][col1])
            decrypted.append(matrix[(row2 - 1) % 5][col2])
        else:
            decrypted.append(matrix[row1][col2])
            decrypted.append(matrix[row2][col1])
    return ''.join(decrypted)