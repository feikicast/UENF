from time import sleep
def menu_hoje():
    print('''---------------------
O que você vai fazer hoje?
[1] Não tomar banho
[2] Tomar banho
---------------------''')

def menu_cel():
    print('''----------------------
Onde você vai deixar o celular?
[1] Fora do box
[2] Na báscula/janela
----------------------''')   

def depilar():
    print('''----------------------
O que você vai usar?
[1] Máquina
[2] Prestobarba
----------------------''') 

def main():
    menu_hoje()
    escolha = int(input(" "))
    if escolha == 2:
        sleep(1)
        print('OK, vamos tomar banho')
        sleep(1)
        print('*pegando a toalha*')
        sleep(1)
        print('*pegando a roupa*')
        sleep(1)
        while True:
            resp_celular = str(input("Você quer pegar seu celular? [S/N] ")).upper()[0]
            if resp_celular == 'S' or resp_celular == 'N':
                break
            else:
                print('Digite apenas S ou N')
        if resp_celular == 'S':
            sleep(1)
            print("*pegando celular*")
            while True:
                sleep(1)
                resp_musica = str(input('Você vai ouvir música no banho? [S/N] ')).upper()[0]  
                if resp_musica == 'S' or resp_musica == 'N':
                    break
                else:
                    print('Digite apenas S ou N')
            if resp_musica == 'S':
                menu_cel()
                while True:
                    resp_deixar_cel = int(input(' '))
                    if resp_deixar_cel == 1 or resp_deixar_cel == 2:
                        break
                    else:
                        print('Digite apenas 1 ou 2')
                if resp_deixar_cel == 2:
                    sleep(1)
                    print('\033[31mSeu celular caiu no chão e explodiu, causando a sua morte.\033[m')
                    exit()
                else:
                    sleep(1)
                    print('Boa escolha.')    
            elif resp_musica == 'N':
                while True:
                    resp_carregar = str(input('Você quer colocar o celular pra carregar? [S/N] ')).upper()[0]
                    if resp_carregar == 'S' or resp_musica == 'N':
                        break
                    else:
                        print('Digite apenas S ou N')
                if resp_carregar == 'S':
                    sleep(1)
                    print('\033[31mSeu celular explodiu e você morreu.\033[m')
                    exit()
                elif resp_carregar == 'N':
                    sleep(1)
                    print('Pegou o celular pra quê então?')
            resp_depilar = str(input('Você vai se depilar hoje? [S/N] ')).upper()[0]
            if resp_depilar == 'S':
                sleep(1)
                depilar()
                while True:
                    resp_depilar_12 = int(input(' '))
                    if resp_depilar_12 == 1 or resp_depilar_12 == 2:
                        break
                if resp_depilar_12 == 1:
                    sleep(1)
                    print('\033[31mAo entrar em contato com a água, a máquina disparou um descarga elétrica e te matou\033[m')
                elif resp_depilar_12 == 2:
                    sleep(1)
                    print('Boa escolha')
                    sleep(1)
                    print('\033[32mVocê encontrou 1 dos 3 finais alternativos em que sairia vivo, será que é capaz de encontrar todos eles?\033[m')
                else:
                    print('Digite apenas 1 ou 2')
            elif resp_depilar == 'N':
                sleep(1)
                print('\033[31mSeu pelo encravou, gerando uma infecção que atingiu a corrente sanguínea, você desenvolveu septicemia e morreu.\033[m')
            else:
                print('Digite apenas S ou N')
        elif resp_celular == 'N':
            sleep(1)
            resp_depilar = str(input('Você vai se depilar hoje? [S/N] ')).upper()[0]
            if resp_depilar == 'S':
                sleep(1)
                depilar()
                while True:
                    resp_depilar_12 = int(input(' '))
                    if resp_depilar_12 == 1 or resp_depilar_12 == 2:
                        break
                if resp_depilar_12 == 1:
                    sleep(1)
                    print('\033[31mAo entrar em contato com a água, a máquina disparou um descarga elétrica e te matou\033[m')
                elif resp_depilar_12 == 2:
                    sleep(1)
                    print('Boa escolha')
                    sleep(1)
                    print('\033[32mVocê encontrou 1 dos 3 finais alternativos em que sairia vivo, será que é capaz de encontrar todos eles?\033[m')
                else:
                    print('Digite apenas 1 ou 2')
            elif resp_depilar == 'N':
                sleep(1)
                print('\033[31mSeu pelo encravou, gerando uma infecção que atingiu a corrente sanguínea, você desenvolveu septicemia e morreu.\033[m')
            else:
                print('Digite apenas S ou N')
    elif escolha == 1:
        sleep(1)
        print('\033[31mApós 1 semana sem tomar banho, você desenvolveu uma infecção e morreu.\033[m')
    elif escolha == 999:
        sleep(1)
        print('OK, então volte a assistir TV')
        sleep(3)
        print('\033[032mCaramba, você é bom! Você encontrou o final secreto!!\033[m')
    else:
        print('Digite apenas 1 ou 2')
main()
