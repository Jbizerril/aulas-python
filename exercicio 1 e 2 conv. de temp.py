def fahrenheit_to_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit."""
    return (celsius * 9 / 5) + 32

def main():
    print("Conversor de Temperatura geral")
    print("Escolha a temperatura:")
    print("1: Converter Fahrenheit para Celsius")
    print("2: Converter Celsius para Fahrenheit")
    # OBS: tentei escrever a palavra 'opção'nas saidas de print do vsc mas os caracteres do português davam erro, no pycharm estava ok, o que fazer no caso?
    # Recebe a escolha do usuário
    escolha = input("Digite 1 ou 2: ")
    
    if escolha == '1':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"A temperatura em Celsius é: {celsius:.2f}")
    elif escolha == '2':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")
    else:
        print("Opção inválida. Por favor, digite 1 ou 2.")

if __name__ == "__main__":
    main()

# pensei em fazer utilizando o comando import para o calculo, deixando o código mais 'sleek' e organizado, algum exemplo que pode ser interessante?
