investimento_inicial = float(input("Digite o investimento inicial: "))
taxa_juros = float(input("Digite a taxa de juros anual (em %): ")) / 100 
anos = int(input("Digite o número de anos: "))
saldo_final = investimento_inicial * (1 + taxa_juros) ** anos

print(f"Após {anos} anos, o valor final é: R${saldo_final:.2f}")
