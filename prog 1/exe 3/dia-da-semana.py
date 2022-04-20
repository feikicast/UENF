from time import sleep

a = 0
while a == 0 or a > 7:
    a = int(input('Digite um valor de 1 a 7: '))
    if a < 1 or a > 7:
        sleep(1.5)
        print('Valor inválido! Tente novamente')
        sleep(1.5)
    if a == 1:
        sleep(1)
        print('Hoje é Domingo')
        break
    if a == 2:
        sleep(1)
        print('Hoje é Segunda')
        break
    if a == 3:
        sleep(1)
        print('Hoje é Terça')
        break
    if a == 4:
        sleep(1)
        print('Hoje é Quarta')
        break
    if a == 5:
        sleep(1)
        print('Hoje é Quinta')
        break
    if a == 6:
        sleep(1)
        print('Hoje é Sexta')
        break
    if a == 7:
        sleep(1)
        print('Hoje é Sábado')
        break
sleep(1)
print('FIM')
