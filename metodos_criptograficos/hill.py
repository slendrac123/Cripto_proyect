import numpy as np
from egcd import egcd

alfabeto = "abcdefghijklmnopqrstuvwxyz"
letra_a_entero = {c: i for i, c in enumerate(alfabeto)}
entero_a_letra = {i: c for i, c in enumerate(alfabeto)}

def clave_a_matriz(clave):
    # Convertir clave a números
    clave_numerica = [letra_a_entero[c] for c in clave.lower() if c in letra_a_entero]

    # Determinar el tamaño de la matriz cuadrada más cercana
    n = int(len(clave_numerica) ** 0.5)
    while n * n < len(clave_numerica):  
        n += 1

    # Rellenar con 'x' (23 en base alfabética) si es necesario
    while len(clave_numerica) < n * n:
        clave_numerica.append(letra_a_entero['x'])

    return np.array(clave_numerica).reshape(n, n)

def egcd(a, b):
    """Algoritmo extendido de Euclides para encontrar el inverso modular."""
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def matriz_inversa(matriz, modulo):
    det = int(np.round(np.linalg.det(matriz)))  # Determinante de la matriz
    det = det % modulo  # Asegurar que está en el rango del módulo

    # Encontrar el inverso del determinante
    gcd, det_inv, _ = egcd(det, modulo)
    if gcd != 1:
        raise ValueError("La matriz no tiene inversa en módulo {}.".format(modulo))

    det_inv = det_inv % modulo

    # Calcular la matriz adjunta y la inversa modular
    matriz_adj = np.round(np.linalg.det(matriz) * np.linalg.inv(matriz)).astype(int) % modulo
    return (det_inv * matriz_adj) % modulo

def hill_cifrar(mensaje, clave):
    matriz_clave = clave_a_matriz(clave)
    n = matriz_clave.shape[0]
    
    # Convertir mensaje a números
    mensaje_numerico = [letra_a_entero[c] for c in mensaje.lower() if c in letra_a_entero]

    # Rellenar con 'x' si es necesario
    while len(mensaje_numerico) % n != 0:
        mensaje_numerico.append(letra_a_entero['x'])

    # Separar en bloques de tamaño n
    mensaje_matriz = np.array(mensaje_numerico).reshape(-1, n).T

    # Multiplicación matricial y reducción módulo 26
    mensaje_cifrado = (np.dot(matriz_clave, mensaje_matriz) % 26).T

    # Convertir números a letras
    return ''.join(entero_a_letra[num] for fila in mensaje_cifrado for num in fila)

def hill_descifrar(mensaje, clave):
    matriz_clave = clave_a_matriz(clave)
    n = matriz_clave.shape[0]
    
    # Obtener la matriz inversa de la clave
    try:
        matriz_clave_inv = matriz_inversa(matriz_clave, 26)
    except ValueError:
        return "Error: La clave no tiene inversa y no se puede descifrar."

    # Convertir mensaje a números
    mensaje_numerico = [letra_a_entero[c] for c in mensaje.lower() if c in letra_a_entero]

    # Separar en bloques de tamaño n
    mensaje_matriz = np.array(mensaje_numerico).reshape(-1, n).T

    # Multiplicación matricial con la inversa y reducción módulo 26
    mensaje_descifrado = (np.dot(matriz_clave_inv, mensaje_matriz) % 26).T

    # Convertir números a letras
    return ''.join(entero_a_letra[num] for fila in mensaje_descifrado for num in fila)
