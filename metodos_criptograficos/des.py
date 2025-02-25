from Crypto.Cipher import DES
import base64

def pad(texto):
    """Añade padding al texto para que sea múltiplo de 8 bytes (DES usa bloques de 64 bits)."""
    while len(texto) % 8 != 0:
        texto += " "
    return texto

def des_cifrar(texto, clave):
    """
    Cifra un mensaje usando el algoritmo DES.
    
    - `texto`: Mensaje a cifrar.
    - `clave`: Debe ser una cadena de 8 caracteres (64 bits).
    - Retorna: Texto cifrado en Base64.
    """
    if len(clave) != 8:
        raise ValueError("La clave para DES debe tener exactamente 8 caracteres.")

    texto = pad(texto)  # Asegurar que el texto tenga tamaño múltiplo de 8
    cipher = DES.new(clave.encode(), DES.MODE_ECB)  # Crear cifrador DES en modo ECB
    texto_cifrado = cipher.encrypt(texto.encode())  # Cifrar el texto
    return base64.b64encode(texto_cifrado).decode()  # Codificar en Base64 para evitar caracteres extraños

def des_descifrar(texto_cifrado, clave):
    """
    Descifra un mensaje cifrado con DES.
    
    - `texto_cifrado`: Mensaje cifrado en Base64.
    - `clave`: Debe ser una cadena de 8 caracteres (64 bits).
    - Retorna: Texto original sin padding.
    """
    if len(clave) != 8:
        raise ValueError("La clave para DES debe tener exactamente 8 caracteres.")

    cipher = DES.new(clave.encode(), DES.MODE_ECB)  # Crear cifrador DES en modo ECB
    texto_cifrado = base64.b64decode(texto_cifrado)  # Decodificar de Base64
    texto_descifrado = cipher.decrypt(texto_cifrado).decode().rstrip()  # Eliminar padding
    return texto_descifrado