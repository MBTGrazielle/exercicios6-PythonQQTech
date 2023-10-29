# 1) A sequencia de Fibonacci é caracterizada por um sequencia de números que começa com 0 e 1, 
# e os próximos termos são os a soma dos dois termos imediatamente anteriores. Por exemplo:

# 1º Termo = 0

# 2º Termo = 1

# 3° Termo = 0+1 = 1

# 4º Termo = 1+1 = 2

# 5º Termo = 1+2 = 3


# a) Calcule os 100 primeiros termos da sequência, colocando-os em uma lista.

fibonacci = [0, 1]

for numero in range(2, 100):
    numero_seguinte = fibonacci[numero - 1] + fibonacci[numero - 2]
    fibonacci.append(numero_seguinte)
    
print(f"Essa é a lista de Fibonacci com os {len(fibonacci)} primeiros termos: {fibonacci}")
print(f"----------------------------------------------------------------------------------------------------------------------------------")

# b) Qual o valor do 59º termo da sequência?

print(f"O 59º primeiro termo é : {fibonacci[59]}")
print(f"----------------------------------------------------------------------------------------------------------------------------------")

# c) Calcule a média aritmética dos 100 primeiros termos da sequencia de Fibonacci. 
# (Lembrando que a média aritmética é dada pela soma de todos os termos dividida pelo número de termos)

soma = sum(fibonacci)
media = soma / len(fibonacci)

print(f"A média aritmética dos {len(fibonacci)} primeiros termos é: {media:.0f}")
print(f"----------------------------------------------------------------------------------------------------------------------------------")


