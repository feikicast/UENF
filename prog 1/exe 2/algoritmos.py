from random import random, randrange
from time import sleep

x = input('Digite o primeiro valor: ')
sleep(1)
y = input('Digite o segundo valor: ')
sleep(1)
print('Processando...')
sleep(2)

a = randrange(-1000000, 1000000)
b = randrange(-1000000, 1000000)

x = a
y = b

print(f'O primeiro valor digitado se tornou {x}')
sleep(2)
print(f'O segundo valor digitado se tornou {y}')
