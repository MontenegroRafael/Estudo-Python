# Programa que leia um numero inteiro e mostre na tela sua tabuada.

# esta foi a minha resolução
"""n = int(input('Digite um número: '))
print('_' * 12)
print('{} x 1 = {}'.format(n, n * 1))
print('{} x 2 = {}'.format(n, n * 2))
print('{} x 3 = {}'.format(n, n * 3))
print('{} x 4 = {}'.format(n, n * 4))
print('{} x 5 = {}'.format(n, n * 5))
print('{} x 6 = {}'.format(n, n * 6))
print('{} x 7 = {}'.format(n, n * 7))
print('{} x 8 = {}'.format(n, n * 8))
print('{} x 9 = {}'.format(n, n * 9))
print('{} x 10 = {}'.format(n, n * 10))
print('-' * 12)
"""

# esta foi a resolução do professor
n = int(input('Digite um número: '))
print('_' * 12)
print('{} x {:2} = {}'.format(n, 1, n * 1))
print('{} x {:2} = {}'.format(n, 2, n * 2))
print('{} x {:2} = {}'.format(n, 3, n * 3))
print('{} x {:2} = {}'.format(n, 4, n * 4))
print('{} x {:2} = {}'.format(n, 5, n * 5))
print('{} x {:2} = {}'.format(n, 6, n * 6))
print('{} x {:2} = {}'.format(n, 7, n * 7))
print('{} x {:2} = {}'.format(n, 8, n * 8))
print('{} x {:2} = {}'.format(n, 9, n * 9))
print('{} x {} = {}'.format(n, 10, n * 10))
print('-' * 12)