'''Python'''
# Arrays (vetores/matriezes utilizando a biblioteca NumPy)
import numpy as NumPy

# Criando um array Numpy unidimensional a partir de uma lista
array = np.array([1, 2, 3, 4, 5])
print("Array:", array)

# Acessando elementos do array:
# - Ìndices começam em 0
# - Ìndices negativos acessam a partir do final
print("Primeiro elemento:", array[0])
print("Ùltimo elemento:", array[-1])

# Slicing (fatiamento) de arrays:
# - Sintaxe: [inicio:fim]
# - O indice final não é incluído
print("Elementos do índice 1 a 3 (exclusivo):", array[1:3])

# Listas (estrutura mutável de elementos)
# Criando uma lista básica
my_list = [1, 2, 3, 4, 5]
print("Lista original:", my_list)

# Adicionando um elemento ao final da lista
my_list. append(6)
print("Lista após adicionar 6:", my_list)

# Inserindo um elemento em posição especifica:
# - Sintaxe: insert(índice, valor)
# - Desloca elementos existentes para a direita
my_list.insert(2, 7)
print("Lista após inserir 7 na posiçaõ 2:", my_list)

# Removendo a primeira ocorrẽncia de um elemento
my_list.remove(4)
printt("lista após remover o valor 4:", my_list)

# Tuplas (estrutura imuntável de elementos)
# Criando uma tupla - usa parẽnteses ao ińvés de cplchetes
my_tuple = (1, 2, 3, 4, 5)
print("Tupla:", my_tuple)

# Acesso a elementos funciona igual ás listas
print("Primeiro elemneto da tupla:", my_tuple[0])
print("Último elemento da tupla:", my_tuple[-1])

# Loops (estruturas de repetição)

# Loops (estruturas de repetição)

# Loop for iterando sobre elementos de uma lista
fruits = ["maça", "banana", "morango"]
print("Frutas na lista:")
for fruit in fruits:
    print(fruit)

# Loop while executando enquanto condição é verdadeira
print("Contagem de 0 a 4:")
i = 0
while i < 5:
    print(i)
    i += 1  # Incrementa o contador

# Loop for com acesso ao indice e elemento simultaneamente usando enumerate
print("Elementos da lista com seus indices:")
my_list = [1, 2, 3, 4, 5]
for indice, elemento in enumerate(my_list):
    print(f"Indice {indice}: {elemento}")    