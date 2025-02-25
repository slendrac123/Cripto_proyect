def generar_clave(texto, clave):
    """Genera una clave repetida hasta que tenga la misma longitud que el texto."""
    clave = clave.upper()
    return (clave * (len(texto) // len(clave))) + clave[:len(texto) % len(clave)]

def vigenere_cifrar(texto, clave):
    """Cifra un mensaje usando el Cifrado Vigenère."""
    clave = generar_clave(texto, clave)
    cifrado = ""

    for i in range(len(texto)):
        if texto[i].isalpha():
            base = 65 if texto[i].isupper() else 97
            desplazamiento = ord(clave[i]) - 65
            cifrado += chr(((ord(texto[i]) - base + desplazamiento) % 26) + base)
        else:
            cifrado += texto[i]  # Mantener caracteres no alfabéticos

    return cifrado

def vigenere_descifrar(texto, clave):
    """Descifra un mensaje cifrado con el Cifrado Vigenère."""
    clave = generar_clave(texto, clave)
    descifrado = ""

    for i in range(len(texto)):
        if texto[i].isalpha():
            base = 65 if texto[i].isupper() else 97
            desplazamiento = ord(clave[i]) - 65
            descifrado += chr(((ord(texto[i]) - base - desplazamiento) % 26) + base)
        else:
            descifrado += texto[i]

    return descifrado