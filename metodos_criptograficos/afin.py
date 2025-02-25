from math import gcd

def mod_inverse(a, m):
    """Calcula el inverso modular de 'a' módulo 'm' si existe."""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def afin_cifrar(texto, a, b):
    """Cifra un mensaje usando el Cifrado Afín."""
    if gcd(a, 26) != 1:
        return "Clave 'a' inválida. Debe ser coprima con 26."

    cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = 65 if caracter.isupper() else 97
            cifrado += chr(((a * (ord(caracter) - base) + b) % 26) + base)
        else:
            cifrado += caracter
    return cifrado

def afin_descifrar(texto, a, b):
    """Descifra un mensaje cifrado con el Cifrado Afín."""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Clave 'a' inválida. No tiene inverso modular."

    descifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = 65 if caracter.isupper() else 97
            descifrado += chr(((a_inv * (ord(caracter) - base - b)) % 26) + base)
        else:
            descifrado += caracter
    return descifrado