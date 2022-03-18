from time import sleep
g = 0
c = 0
while True:
    print('O que você vai fazer hoje?')
    print('[1] Não tomar banho')
    print('[2] Tomar banho')
    a = input('')
    if a == '2':
        sleep(1.5)
        print('OK, vamos tomar banho')
        sleep(1.5)
        print('*pegando a toalha*')
        sleep(1.5)
        print('*pegando a roupa*')
        sleep(1.5)
        b = input('Pegar o celular? [Sim/Não] ')
        if b in 'SsSimSIMsim':
            sleep(1.5)
            print('*pegando o celular*')
            sleep(1.5)
            e = input('Você vai ouvir música no banho? [Sim/Não] ')
            if e in 'nNãoNnãoNÃO':
                sleep(1.5)
                f = input('Você quer colocar o celular pra crregar? [Sim/Não] ')
                if f in 'nNãoNnãoNÃO':
                    sleep(1.5)
                    print('Pegou celular pra quê então?')
                elif f in 'SsSimSIMsim':
                    sleep(1.5)
                    print('\033[31mSeu celular é Samsung, ele explodiu e você morreu.\033[m')
                    break
                else:
                    sleep(1.5)
                    print('\033[33mPor favor, digite um valor válido.\033[m')
            if e in 'SsSimSIMsim':
                sleep(1.5)
                print('Onde você vai deixar o celular?')
                print('[1] Fora do box')
                print('[2] Na báscula/janela')
                g = input('')
                if g == '2':
                    print('\033[31mSeu celular caiu no chão e explodiu, causando a sua morte.\033[m')
                    break
                elif g != '1' or '2':
                    print('\033[33mPor favor, digite um valor válido.\033[m')
            sleep(1.5)
            c = input('Você vai se depilar hoje? [Sim/Não] ')
            if c in 'SsSimSIMsim':
                sleep(1.5)
                print('O que você vai usar?')
                print('[1] Máquina')
                print('[2] Prestobarba')
                d = input('')
            elif c in 'nNãoNnãoNÃO':
                sleep(1.5)
                print('\033[31mSeu pelo encravou, gerando uma infecção que atingu a corrente sanguínea, você desenvolveu septicemia e morreu.\033[m')
                break
            else:
                print('\033[33mPor favor, digite um valor válido.\033[m')
        elif b in 'nNãoNnãoNÃO':
            sleep(1.5)
            c = input('Você vai se depilar hoje? [Sim/Não] ')
            if c in 'SsSimSIMsim':
                sleep(1.5)
                print('O que você vai usar?')
                print('[1] Máquina')
                print('[2] Prestobarba')
                d = input('')
            elif c in 'nNãoNnãoNÃO':
                sleep(1.5)
                print('\033[31mSeu pelo encravou, gerando uma infecção que atingu a corrente sanguínea, você desenvolveu septicemia e morreu.\033[m')
            else:
                print('\033[33mPor favor, digite um valor válido.\033[m')
        else:
            print('\033[33mPor favor, digite um valor válido.\033[m')
    elif a == '1':
        sleep(1.5)
        print('\033[31mApós 1 semana sem tomar banho, você desenvolveu uma infecção e morreu.\033[m')
        break
    else:
        print('\033[33mPor favor, digite um valor válido.\033[m')
    sleep(1.5)
    if g == '1' and c in'1':
        sleep(1.5)
        print('*ligando o chuveiro*')
        sleep(1.5)
        print('*se molhando*')
        sleep(1.5)
        print('*se ensaboando*')
        sleep(1.5)
        print('*ligando a máquina*')
        sleep(1.5)
        print('*começando a se depilar*')
        sleep(1.5)
        print('*a água entrou na máquina*')
        sleep(1.5)
        print('\033[31mVocê morreu eletrocutado.\033[m')
        break
    if g == '1' and c in'2':
        sleep(1.5)
        print('*ligando o chuveiro*')
        sleep(1.5)
        print('*se molhando*')
        sleep(1.5)
        print('*se ensaboando*')
        sleep(1.5)
        print('*pegando o prestobarba*')
        sleep(1.5)
        print('*começando a se depilar*')
        sleep(1.5)
        print('*terminando de se depilar*')
        sleep(1.5)
        print('*se limpando*')
        sleep(1.5)
        print('*pegando a toalha*')
        sleep(1.5)
        print('*se secando*')
        sleep(1.5)
        print('*colocando a roupa*')
        sleep(1.5)
        print('*FIM*')
        break
