def cesar_cifrar(texto, clave):
    """Cifra un mensaje usando el Cifrado César."""
    cifrado = ""
    clave = int(clave)
    for caracter in texto:
        if caracter.isalpha():
            desplazamiento = 65 if caracter.isupper() else 97
            cifrado += chr((ord(caracter) - desplazamiento + clave) % 26 + desplazamiento)
        else:
            cifrado += caracter
    return cifrado

def cesar_descifrar(texto, clave):
    """Descifra un mensaje cifrado con el Cifrado César."""
    return cesar_cifrar(texto, -int(clave))