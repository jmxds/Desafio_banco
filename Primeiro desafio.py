Mensagem = f'''
########################  Bem-Vindo ao Banco Tape Co. #################################

                        Menu:
                
                        Qual ação deseja realizar?

                        [1] Sacar
                        [2] Depositar
                        [3] Checar Extrato
                        [4] Sair

########################################################################################
'''

saldo = 10.00
limite = 500.00
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3





while True:
    print(Mensagem)
    menu = int(input("\n"))

    if menu == 1:
        print("Saque Selecionado")
        saque = float(input("Insira o Valor que deseja sacar\n"))
        saque_valido = False
        while saque_valido == False:
            if saque > saldo:
                print(f"Não foi possível realizar o saque pois o valor solicitado é maior do que o valor do saldo.\n Saldo atual: R${saldo:.2f}")
                choice_1 = input('Deseja sacar outro valor? [s] / [n]\n')
                
            
            if saque > limite:
                print(f"Não foi possível realizar o saque pois o valor solicitado está acima do valor limite. Valor limite atual: R${limite:.2f}")
                choice_1 = input('Ainda deseja sacar? [s] / [n]')
                
            if saque <= 0.00:
                print(f"Não é possível sacar o valor {saque:.2f}\n Favor inserir um valor válido")
                choice_1 = input('Ainda deseja sacar? [s] / [n]')
                
            if numero_de_saques>= LIMITE_SAQUES:      
                print(f"Não foi possível realizar o saque pois o limite de saques diários foi atingido.")
                break
            
            if saque < limite and saque > 0.00 and saque <= saldo and numero_de_saques <= 3:
                saque_valido = True  
            else:    
                while choice_1 != 's' and choice_1 != 'S' and choice_1 != 'n' and choice_1 != 'N':
                    print('Insira um valor válido!')
                    choice_1 = input('Deseja sacar outro valor? [s] / [n]\n')
                if choice_1 == 'n' or choice_1 == 'N':
                    break
                elif choice_1 == 's' or choice_1 == 'S':
                    saque = float(input("Insira o Valor que deseja sacar\n"))
            
        
        if saque_valido == True:
            saldo -= saque
            numero_de_saques+=1
            print(f" Saque realizado com sucesso \n \n Saldo atual {saldo:.2f}")

    elif menu == 2:
        print("Depósito Selecionado")
        deposito = float(input("Insira o Valor que deseja depositar"))
        while deposito<=0:
                print("Insira um valor de depósito válido")
                deposito = float(input("Insira o Valor que deseja depositar"))
        saldo += deposito

        print(f" Depósito realizado com sucesso \n \n Saldo atual {saldo:.2f}")
    elif menu == 3:
        print("Extrato")
    elif menu == 4:
        print("Fim da Seção".center(10,'#'))
        break
    else:
        print("Comando Inválido")
