import random

def simular_mega_sena():
    print("Bem-vindo ao concurso da Mega-Sena! Aperte a tecla Enter para continuar e tentar sua sorte!.")
    input()  

# OBS: na parte de input dos numeros fiquei na dúvida se seria possivel com que o programa ignorase se o usuario não colocasse espaço ou colocasse virgulas, seria possivel?

    while True:
        sorteados = sorted(random.sample(range(1, 61), 6))
        print(f"Números sorteados: {sorteados}")
        
        try:
            aposta = sorted(set(int(num) for num in input("Digite 6 números distintos entre 1 e 60: ").split() if 1 <= int(num) <= 60))
            if len(aposta) != 6:
                raise ValueError
        except ValueError:
            print("Entrada inválida. Tente novamente.Por favor, coloque apenas 6 números")
            continue
        
        acertos = len(set(sorteados) & set(aposta))
        print(f"Você acertou {acertos} números. {'Sena!' if acertos == 6 else 'Quina!' if acertos == 5 else 'Quadra!' if acertos == 4 else 'Infelizmente, não ganhou desta vez.'}")
        
        if input("Gostaria de tentar um novo sorteio? (s/n): ").strip().lower() != 's':
            print("Obrigado por tentar a Sorte na Mega Sena!")
            break

# OBS: Para deixar mais 'realista' o programa, coloquei mensagens no começo do código e no final, ao terminar
# OBS final: embora no VSCode rodou sem problema, rapidinho, eu vi um pequeno delay testando no pycharm, seria problema do aplicativo em si ou algum erro nas variables do código que poderia estar deixando ele lento?

simular_mega_sena()