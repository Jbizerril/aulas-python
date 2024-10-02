import math

def calcular_fatorial(n):
    if n < 0:
        return "O fatorial não é válido para números negativos."
    else:
        return math.factorial(n)

numero = int(input("Digite um número para calcular o fatorial: "))

resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")