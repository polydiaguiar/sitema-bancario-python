
menu = """
Escolha umas das opções do menu a seguir: 

========= Menu =========

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair 

=========================

=> """


saldo = 0
limite = 500
extrato = " "
numero_de_saques = 0
LIMITE_SAQUES = 3


def gramatica_real(valor):

    if valor == 1:
        return (" real.")
    else:
        return(" reais.")


while True:

    opcao = int(input(menu))
    
    if opcao == 0: 
        #converte valor para float e atribui à variável valor_depositado
        valor = float(input("Digite o valor que deseja depositar. Operação permitida apenas com cédula.\n=> "))

        #atualiza saldo e retorna extrato atualizado
        if valor >0:
            saldo += valor
            extrato += f"\nDepósito: R${valor: .2f} {gramatica_real(valor)}"
            print("Operação concluída com sucesso!")
        
        #barra depositos de valores menores que zero
        else:
            print("Valor inválido. Operação não concluída")
        
  

    elif opcao == 1:
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor>saldo

        excedeu_limite = valor>limite

        excedeu_limite_saques = numero_de_saques >=LIMITE_SAQUES


        if excedeu_saldo:
            
            print("\nOperação falhou. Você não tem saldo suficiente.")
            
        elif excedeu_limite:

            print("\nOperação falhou. Valor solicitado é superior ao valor máximo de saque permitido para sua conta.")

        elif excedeu_limite_saques:

            print("\nOperação não concluída. Você excedeu o limite de saques diários.")

        elif valor>0:
            saldo -= valor
            extrato += f"\nSaque: R${valor:.2f} {gramatica_real(valor)}"
            numero_de_saques +=1
            print("Operação concluída com sucesso. Retire o dinheiro na boca do caixa eletrônico.")     
     
        else:
            print("Operação falhou. Valor solicitado inválido.")
  
    elif opcao == 2:
        
        print(" \n============ EXTRATO ============ ")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}{gramatica_real(valor==saldo)}")
        print("=================================")

    elif opcao == 3 :
        break

    else:
        print("\nOperação inválida, por favor selecionar novamente a operação desejada.\n=> ")






