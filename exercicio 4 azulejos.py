import math

def calcular_caixas(comprimento, altura, tamanho_azulejo, azulejos_por_caixa, num_paredes):
    area_total = comprimento * altura * num_paredes
    area_caixa = tamanho_azulejo * azulejos_por_caixa
    return math.ceil(area_total / area_caixa)

def main():
    comprimento = float(input("Comprimento da parede (m): "))
    altura = float(input("Altura da parede (m): "))
    tamanho_azulejo = float(input("Tamanho de cada azulejo (m²): "))
    azulejos_por_caixa = int(input("Número de azulejos por caixa: "))
    num_paredes = int(input("Número de paredes a serem cobertas: "))

#OBS, queria fazer algo mais complexo, inclusive o desafio, mas meio que como nunca mexi com azulejos e medidas do mesmo para obras, estou, por enquanto sem ideias nesse.

    numero_caixas = calcular_caixas(comprimento, altura, tamanho_azulejo, azulejos_por_caixa, num_paredes)
    print(f"Número de caixas necessárias: {numero_caixas}")

if __name__ == "__main__":
    main()