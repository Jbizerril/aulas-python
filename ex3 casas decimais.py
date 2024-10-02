numero = float(input("Digite um número decimal: "))

casas_decimais = int(input("Digite o número de casas decimais desejado: "))

numero_formatado = f"{numero:.{casas_decimais}f}"

print(f"O número formatado com {casas_decimais} casas decimais é: {numero_formatado}")
