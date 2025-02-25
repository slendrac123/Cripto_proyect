import tkinter as tk
from tkinter import ttk, messagebox
from metodos_criptograficos import cesar, afin, vigenere, hill, playfair, permutacion, aes, des, elgamal


def procesar(accion):
    texto = entrada_texto.get("1.0", tk.END).strip()
    clave = entrada_clave.get().strip()

    if not texto:
        messagebox.showwarning("Advertencia", "El texto no puede estar vacío.")
        return

    metodo = metodo_var.get()

    try:
        if metodo == "César":
            if not clave.isdigit():
                raise ValueError("La clave debe ser un número.")
            clave = int(clave)
            resultado = cesar.cesar_cifrar(texto, clave) if accion == "Cifrar" else cesar.cesar_descifrar(texto, clave)

        elif metodo == "Afín":
            clave_partes = clave.split(",")
            if len(clave_partes) != 2 or not clave_partes[0].isdigit() or not clave_partes[1].isdigit():
                raise ValueError("La clave para Afín debe ser 'a,b' (dos números).")
            a, b = int(clave_partes[0]), int(clave_partes[1])
            resultado = afin.afin_cifrar(texto, a, b) if accion == "Cifrar" else afin.afin_descifrar(texto, a, b)

        elif metodo == "Vigenère":
            if not clave.isalpha():
                raise ValueError("La clave de Vigenère solo puede contener letras.")
            resultado = vigenere.vigenere_cifrar(texto, clave) if accion == "Cifrar" else vigenere.vigenere_descifrar(texto, clave)

        elif metodo == "Hill":
            if len(clave) not in {4, 9}:
                raise ValueError("La clave de Hill debe tener 4 o 9 letras (matriz 2x2 o 3x3).")
            resultado = hill.hill_cifrar(texto, clave) if accion == "Cifrar" else hill.hill_descifrar(texto, clave)
        
        elif metodo == "Playfair":
            if not clave.isalpha():
                raise ValueError("La clave de Playfair solo puede contener letras.")
            resultado = playfair.playfair_cifrar(texto, clave) if accion == "Cifrar" else playfair.playfair_descifrar(texto, clave)


        elif metodo == "Permutación":
            clave_partes = clave.split(",")
            for c in clave_partes:
                if not c.isdigit() or clave.isdigit():
                    raise ValueError("La clave de Permutación debe ser una lista de números separados por comas.")
            resultado = permutacion.permutacion_cifrar(texto, clave) if accion == "Cifrar" else permutacion.permutacion_descifrar(texto, clave)

        elif metodo == "AES":
            resultado = aes.aes_cifrar(texto, clave) if accion == "Cifrar" else aes.aes_descifrar(texto, clave)
        
        elif metodo == "DES":
            resultado = des.des_cifrar(texto, clave) if accion == "Cifrar" else des.des_descifrar(texto, clave)
        

        else:
            raise ValueError("Método no soportado.")

        salida_texto.delete("1.0", tk.END)
        salida_texto.insert(tk.END, resultado)

    except ValueError as e:
        messagebox.showwarning("Error", str(e))

# Crear ventana
root = tk.Tk()
root.title("Codificación")
root.geometry("500x400")

# Etiqueta del método
ttk.Label(root, text="Método de Codificación:").pack(pady=5)
metodo_var = tk.StringVar(value="César")
ttk.Combobox(root, textvariable=metodo_var, values=["César", "Afín", "Vigenère", "Hill", "Playfair", "Permutación", "AES", "DES"]).pack()

# Área de entrada de texto
ttk.Label(root, text="Texto:").pack(pady=5)
entrada_texto = tk.Text(root, height=4, width=50)
entrada_texto.pack()

# Clave
ttk.Label(root, text="Clave:").pack(pady=5)
entrada_clave = ttk.Entry(root)
entrada_clave.pack()

# Botones
ttk.Button(root, text="Cifrar", command=lambda: procesar("Cifrar")).pack(pady=5)
ttk.Button(root, text="Descifrar", command=lambda: procesar("Descifrar")).pack()

# Área de salida de texto
ttk.Label(root, text="Resultado:").pack(pady=5)
salida_texto = tk.Text(root, height=4, width=50, state="normal")
salida_texto.pack()

# Iniciar la aplicación
root.mainloop()
