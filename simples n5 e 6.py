def classificar_numero(numero):
    if numero > 0:
        return "O número é positivo."
    elif numero < 0:
        return "O número é negativo."
    else:
        return "Zero"

def main():
    numero = float(input("Digite um número: "))
    resultado = classificar_numero(numero)
    print(resultado)

main()