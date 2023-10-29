# 2) Faça uma função que calcule a sequência de fibonacci até o n-ésimo termo, sendo n um argumento 
# que será passado pra função. Faça essa função retornar uma lista com os termos calculados dentro.

def sequencia_fibonacci(n):
    fibonacci = [0, 1]

    for numero in range(2, n):
        numero_seguinte = fibonacci[numero - 1] + fibonacci[numero - 2]
        fibonacci.append(numero_seguinte)

    return fibonacci

sequencia_fibonacci = sequencia_fibonacci(99)

print(f"Esta é a lista de Fibonacci com os {len(sequencia_fibonacci)} primeiros termos: {sequencia_fibonacci}")



