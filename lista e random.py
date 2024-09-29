import random

lista_numeros = []

for i in range (11):
    numeros_random = random.randint(1,10)
    numeroQuadrado = numeros_random ** 2
    lista_numeros.append(numeroQuadrado)

soma = sum(lista_numeros)

print(f"A lista de números sorteados é: {lista_numeros}")
print(f"A soma dos elementos da lista é: {soma}")
