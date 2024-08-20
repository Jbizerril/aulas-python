import math

# OBS: utilizei a função import nessa atividade para tentar deixar um código mais compacto

def calcular_lampadas(comprimento, largura, potencia_lampada):
    area = comprimento * largura
    iluminacao_necessaria = area * 100
    lumens_por_lampada = potencia_lampada * 100  # Assumindo 100 lúmens por watt, admito que não sou da area de eletrica então meio que fui no chute
    return math.ceil(iluminacao_necessaria / lumens_por_lampada)

# OBS 2: como se tratava de buscar medidas e lampadas em certos ambientes, achei interessante tentar criar um código que tivesse função de 'loop', para caso do usuario quiser mexer em varias salas dentro de uma casa, escritório, etc


def main():
    while True:
        comprimento = float(input("Qual é o comprimento da sala? (m): "))
        largura = float(input("E qual seria aLargura da sala? (m): "))
        potencia_lampada = float(input("Potência da lâmpada (watts): "))

        numero_lampadas = calcular_lampadas(comprimento, largura, potencia_lampada)
        print(f"O número de lâmpadas necessárias é: {numero_lampadas}")

        repetir = input("Deseja calcular para outra sala? (s/n): ").strip().lower()
        if repetir != 's':
            break


if __name__ == "__main__":
    main()