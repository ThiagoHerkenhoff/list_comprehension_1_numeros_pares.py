"""
Dada uma lista de números inteiros, crie uma nova lista que contenha apenas os
números pares elevados ao quadrado.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Dica: Lembre-se de usar a operação de módulo (%) para verificar se um número é par.

"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = [num ** 2 for num in numeros if num % 2 == 0]

print(numeros_pares)