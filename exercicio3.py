# 3) Utilizando a função criada no exercício anterior, crie 2 arquivos de texto, um com o nome 
# *10_termos.txt* que contenha os 10 primeiros termos da sequência de Fibonacci, um termo em cada linha, 
# e outro arquivo *100_termos.txt* com os 100 primeiros termos da sequência.

# Função para calcular a sequência de Fibonacci
def sequencia_fibonacci(n):
    fibonacci = [0, 1]

    for numero in range(2, n):
        numero_seguinte = fibonacci[numero - 1] + fibonacci[numero - 2]
        fibonacci.append(numero_seguinte)

    return fibonacci

sequencia_10 = sequencia_fibonacci(10)

with open('10_termos.txt', 'w') as arquivo_10:
    for termo in sequencia_10:
        arquivo_10.write(f"{termo}\n")
        
sequencia_100 = sequencia_fibonacci(100)

with open('100_termos.txt', 'w') as arquivo_100:
    for termo in sequencia_100:
        arquivo_100.write(f"{termo}\n")


