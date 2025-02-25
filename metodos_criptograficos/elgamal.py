from Crypto.PublicKey import ElGamal
from Crypto.Random import get_random_bytes
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Hash import SHA256

def elgamal_generate_keys():
    """
    Genera un par de claves ElGamal.
    
    :return: Una tupla con la clave pública y la clave privada.
    """
    key = ElGamal.generate(2048, get_random_bytes)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key

def elgamal_cifrar(texto, public_key):
    """
    Cifra un mensaje usando ElGamal.
    
    :param texto: Texto a cifrar.
    :param public_key: Clave pública de ElGamal.
    :return: Texto cifrado.
    """
    key = ElGamal.import_key(public_key)
    h = SHA256.new(texto.encode())
    k = get_random_bytes(16)
    ciphertext = key.encrypt(bytes_to_long(h.digest()), k)
    return ciphertext

def elgamal_descifrar(texto_cifrado, private_key):
    """
    Descifra un mensaje cifrado con ElGamal.
    
    :param texto_cifrado: Texto cifrado.
    :param private_key: Clave privada de ElGamal.
    :return: Texto descifrado.
    """
    key = ElGamal.import_key(private_key)
    plaintext = key.decrypt(texto_cifrado)
    return long_to_bytes(plaintext).decode()

"""
P = 162259276829213363391578010288127  # Número primo grande
G = 5  # Generador
H = 94857859567237410923492834792374  # H = G^X mod P

X = 987654321987654321  # Clave privada secreta
"""