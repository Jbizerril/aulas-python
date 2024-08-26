def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_aprovacao(media):
    if media >= 6.0:
        return f"Aprovado com média {media:.2f} Parabéns!"
    else:
        return f"Reprovado com média {media:.2f}."


def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = calcular_media(nota1, nota2)
    resultado = verificar_aprovacao(media)
    print(resultado)


main()