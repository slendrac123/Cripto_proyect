from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def aes_cifrar(texto, clave):
    """
    Cifra un mensaje usando AES en modo CBC.

    :param texto: Texto plano a cifrar.
    :param clave: Clave de 16, 24 o 32 bytes.
    :return: Texto cifrado en Base64.
    """
    clave = clave.encode('utf-8')  # Convertir clave a bytes
    if len(clave) not in {16, 24, 32}:
        raise ValueError("La clave debe tener 16, 24 o 32 caracteres.")

    iv = AES.block_size * b'\x00'  # Usamos un IV fijo de 16 bytes (mejor usar un IV aleatorio en producción)
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    
    texto_bytes = texto.encode('utf-8')
    texto_cifrado = cipher.encrypt(pad(texto_bytes, AES.block_size))
    
    return base64.b64encode(texto_cifrado).decode('utf-8')  # Convertir a Base64 para facilitar su almacenamiento

def aes_descifrar(texto_cifrado, clave):
    """
    Descifra un mensaje cifrado con AES en modo CBC.

    :param texto_cifrado: Texto cifrado en Base64.
    :param clave: Clave de 16, 24 o 32 bytes.
    :return: Texto descifrado.
    """
    clave = clave.encode('utf-8')
    if len(clave) not in {16, 24, 32}:
        raise ValueError("La clave debe tener 16, 24 o 32 caracteres.")

    iv = AES.block_size * b'\x00'  # Usamos el mismo IV que en el cifrado
    cipher = AES.new(clave, AES.MODE_CBC, iv)

    texto_cifrado_bytes = base64.b64decode(texto_cifrado)
    texto_descifrado = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size)
    
    return texto_descifrado.decode('utf-8')