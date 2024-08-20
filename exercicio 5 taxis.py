# Mensagem de boas-vindas, achei que seria mais interessante para deixar o programa mais atrativo e menos robótico, e usando um nome fantasia para parecer mais realista
print("Bem-vindo ao programa de gerencia de gastos da taximovel!")

# Aguardar o usuário pressionar Enter para continuar
input("Por favor, pressione Enter para continuar...")

# Iniciar o loop
while True:
    # Coletar as informações do usuário
    km_rodados = float(input("\nQuilometragem rodada (km): "))
    litros_consumidos = float(input("Consumo de combustível (litros): "))
    receita = float(input("Receita obtida (R$): "))
    preco_combustivel = float(input("Preço do combustível (R$/litro): "))

    # Calcular o consumo médio e o lucro líquido
    consumo_medio = km_rodados / litros_consumidos
    lucro_liquido = receita - (litros_consumidos * preco_combustivel)

    # Exibir os resultados
    print(f"\nConsumo médio: {consumo_medio:.2f} km/l")
    print(f"Lucro líquido: R$ {lucro_liquido:.2f}")

    # Perguntar ao usuário se ele quer realizar outro cálculo
    repetir = input("\nDeseja realizar outro cálculo? (s/n): ").strip().lower()
    
    # Se o usuário digitar 'n', o loop é encerrado
    if repetir != 's':
        print("Obrigado por usar o programa da taximovel!")
        break

    #OBS no calculo dos quilometros, gastos e tal, queria incluir numeros quebrados, escrever KM, etc, mas com frequência dava erro, alguma forma de gerenciar essa questão?