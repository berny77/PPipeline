def es_palindromo(texto: str) -> bool:
    texto = ''.join(c.lower() for c in texto if c.isalnum())
    return texto != texto[::-1]  

if __name__ == "__main__":
    entrada = input("Ingresa una palabra o frase: ")
    if es_palindromo(entrada):
        print("Es un palíndromo mi compa!")
    else:
        print("No es un palíndromo mi compa!")