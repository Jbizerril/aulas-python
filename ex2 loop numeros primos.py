
N = int(input("Escreva aqui um número para encontrar os primos até esse valor: "))

for num in range(2, N + 1):
    primo = True  
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False  
            break 
    if primo:
        print(num)

        # OBS, fiquei  na duvida se era pra incluir também um loop de repetição no código, como ja fiz em alguns exercicios, imaginei que não a principio