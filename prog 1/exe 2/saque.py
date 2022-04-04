from time import sleep

print('='*20)
sleep(1)
print('{:^20}'.format('FeikiCash'))
sleep(1)
print('='*20)
sleep(0.5)

valor = int(input('Quanto você deseja sacar? R$'))
sleep(2)
print('Processando...')
sleep(2)
total = valor
ced = 100
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            if totced > 1:
                print(f'{totced} céculas de R${ced}')
                sleep(2)
            elif totced == 1:
                print(f'{totced} cécula de R${ced}')
                sleep(2)
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if total == 0:
            break
