# 1 VA - Q2.
# Programa em Python para implementação do Heapsort.

def heapsort (array, n, i):
    maior = i # Raiz
    ma = 2 * i + 1 # Esquerda
    me = 2 * i + 2 # Direita

# Verificando se os valores à esquerda são maiores que 
# a raiz. 

    if ma < n and array[i] < array[ma]:
        maior = ma 
# Verificando se os valores à direita são maiores que 
# a raiz.

    if me < n and array[maior] < array[me]:
        maior = me

# Caso necessário, trocar a raiz.

    if maior != i:
        array[i], array[maior] = array[maior], array[i]
        heapsort(array, n, maior)

#Função de Ordenação do Algoritmo.

def heapsortTest(array):
    n = len(array)

# Aqui definimos a heap máxima.

    for i in range(n // 2 - 1, - 1, - 1):
        heapsort(array, n, i)

# Verificando elementos um por um.

    for i in range(n - 1, 0, - 1):
        array[i], array[0] = array[0], array[i]
        heapsort(array, i, 0)

#Teste Final. Fazendo a ordenação dos valores.
# Vetor ordenado: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
# Vetor não ordenado: 10, 7, 5, 3, 4, 9, 6, 1, 2, 8.

array = [10, 7, 5, 3, 4, 9, 6, 1, 2, 8]
heapsortTest(array)
n = len(array)
print ("Vetor: ")
for i in range(n):
    print ("%d" %array[i])

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
heapsortTest(array)
n = len(array)
print ("Vetor: ")
for i in range(n):
    print ("%d" %array[i])