def cifrar_rot13(texto):
    resultado = ""
    for char in texto:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
        else:
            resultado += char
    return resultado

def descifrar_rot13(texto):
    return cifrar_rot13(texto)

def main():
    opcion = input("¿Quieres cifrar o descifrar? (c/d): ").lower()

    if opcion == 'c':
        mensaje = input("Ingrese el mensaje a cifrar: ")
        mensaje_cifrado = cifrar_rot13(mensaje)
        print("\nMensaje cifrado:", mensaje_cifrado)
    elif opcion == 'd':
        mensaje = input("Ingrese el mensaje a descifrar: ")
        mensaje_descifrado = descifrar_rot13(mensaje)
        print("\nMensaje descifrado:", mensaje_descifrado)
    else:
        print("Opción no válida. Debes elegir 'c' para cifrar o 'd' para descifrar.")

if __name__ == "__main__":
    main()
