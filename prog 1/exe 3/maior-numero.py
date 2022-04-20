from time import sleep

x = 0

for c in range(1, 4):
    a = float(input(f'Digite o {c}° número: '))
    sleep(1)
    if a > x:
        x = a

sleep(1)
print('Processando...')
sleep(1.5)
print(f'O maior número digitado foi {x}')
