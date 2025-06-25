import time

Mensagem = f'''
########################  Bem-Vindo ao Banco Tape Bank #################################

                        Menu:
                
                        Qual ação deseja realizar?

                        [1] Sacar
                        [2] Depositar
                        [3] Checar Extrato
                        [4] Sair

########################################################################################
'''


fim = f'''
########################################################################################




                                Fim da Sessão




#########################################################################################


'''

saldo = 0.00
limite = 500.00
extrato = []
numero_de_saques = 0
LIMITE_SAQUES = 3





while True:
    print(Mensagem)
    menu = int(input("\n"))

    if menu == 1:
        if numero_de_saques>= LIMITE_SAQUES:      
                print(f"Não foi possível realizar o saque pois o limite de saques diários foi atingido.")
                time.sleep(3)
                
        elif saldo == 0.00:
            print("Não há saldo para saque")
            time.sleep(2)
            
        else:
            print("Saque Selecionado")
            saque = float(input("Insira o Valor que deseja sacar\n"))
            saque_valido = False
            
            while saque_valido == False:
                if saque > saldo:
                    print(f"Não foi possível realizar o saque pois o valor solicitado é maior do que o valor do saldo.\n Saldo atual: R$ {saldo:.2f}")
                    choice_1 = input('Deseja sacar outro valor? [s] / [n]\n')
                    
                
                if saque > limite:
                    print(f"Não foi possível realizar o saque pois o valor solicitado está acima do valor limite. Valor limite atual: R$ {limite:.2f}")
                    choice_1 = input('Ainda deseja sacar? [s] / [n]\n')
                    
                if saque <= 0.00:
                    print(f"Não é possível sacar o valor R$ {saque:.2f}\n Favor inserir um valor válido")
                    choice_1 = input('Ainda deseja sacar? [s] / [n]\n')
                    
            
                
                if saque <= limite and saque > 0.00 and saque <= saldo:
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
                extrato.append(f"Saque: R$ {saque:.2f} Saldo - R$ {saldo:.2f}")
                print(f" Saque realizado com sucesso \n \n Saldo atual R$ {saldo:.2f}")
                time.sleep(3)

    elif menu == 2:
        print("Depósito Selecionado")
        deposito = float(input("Insira o Valor que deseja depositar\n"))
        while deposito<=0.00:
                print("Insira um valor de depósito válido")
                deposito = float(input("Insira o Valor que deseja depositar\n"))
        saldo += deposito
        extrato.append(f"Depósito: R$ {deposito:.2f} Saldo - R$ {saldo:.2f}")

        print(f" Depósito realizado com sucesso \n \n Saldo atual R$ {saldo:.2f}")
        time.sleep(3)
    elif menu == 3:
        if extrato == []:
            print('Ainda não houve movimentação na conta!')
            time.sleep(3)
        else:
            print(f"\nExtrato:")
            for trasancoes in extrato:
                print(trasancoes)

            print(f"\n Saldo Atual: R$ {saldo:.2f}")
            time.sleep(5)
            
    elif menu == 4:
        print(fim)
        break
    else:
        print("Comando Inválido")
        time.sleep(2)
