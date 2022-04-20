from time import sleep

vogal = 'A, E, I, O, U'

x = str(input('Digite 1 letra: ')).strip().upper()[0]
sleep(1)

if x in vogal:
    print(f'Você digitou a vogal {x}')
elif x not in vogal:
    print(f'Você digitou a consoante {x}')

sleep(1.5)
print('FIM')
