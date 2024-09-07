#atribuição variável menu
menu = """
Escolha umas das opções do menu a seguir: 

========= Menu =========

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair 

=========================

=> """

#atribuição de variáveis e contante
saldo = 0
limite = 500
extrato = " "
numero_de_saques = 0
LIMITE_SAQUES = 3

#função para plural da palavra real
def gramatica_real(valor):

    if valor == 1:
        return (" real.")
    else:
        return(" reais.")

#inicia loop 
while True:
    #atribui à variável opção o valor inputado em menu
    opcao = int(input(menu))
    
    #define condicional para depósito
    if opcao == 0: 
        #converte 'valor' para float 
        valor = float(input("Digite o valor que deseja depositar. Operação permitida apenas com cédula.\n=> "))

        if valor >0:        #atualiza saldo e retorna extrato atualizado
            saldo += valor
            extrato += f"\nDepósito: R${valor: .2f} {gramatica_real(valor)}"
            print("Operação concluída com sucesso!")
        
        #barra depositos de valores menores que zero
        else:
            print("Valor inválido. Operação não concluída")
        

    elif opcao == 1:  #define condicional para saque
        
        valor = float(input("Informe o valor do saque: "))         #converte 'valor' para float 

        excedeu_saldo = valor > saldo #atribui regra de validação para a variável excedeu_saldo
        excedeu_limite = valor > limite         #atribui regra de validação para a variável excedeu_limite
        excedeu_limite_saques = numero_de_saques >= LIMITE_SAQUES         #atribui regra de validação para a variável excedeu_limite_saques

        if excedeu_saldo: #condicional para a condição excedeu saldo verdadeira
            
            print("\nOperação falhou. Você não tem saldo suficiente.")
        
        elif excedeu_limite:         #condicional para a condição excedeu limite verdadeira

            print("\nOperação falhou. Valor solicitado é superior ao valor máximo de saque permitido para sua conta.")

        #condicional para a condição excedeu limite saques
        elif excedeu_limite_saques:

            print("\nOperação não concluída. Você excedeu o limite de saques diários.")
 
        elif valor>0:  #validar valor do saque
            
            saldo -= valor #atualiza valor do saldo
            extrato += f"\nSaque: R${valor:.2f} {gramatica_real(valor)}" #atualiza extrato, saque com 02 cadas decimais e chama função para a palavra real
            numero_de_saques +=1 #contabiliza número de saques
            print("Operação concluída com sucesso. Retire o dinheiro na boca do caixa eletrônico.")     
     
        #retorno para o não atendimento de nenhuma das condições acima
        else:
            print("Operação falhou. Valor solicitado inválido.")
  
    #condicional para extrato
    elif opcao == 2:
        
        print(" \n============ EXTRATO ============ ")
        print("Não foram realizadas movimentações." if not extrato else extrato) 
        print(f"\nSaldo: R${saldo:.2f}{gramatica_real(valor==saldo)}")
        print("=================================")

    #condicional para sair da aplicação
    elif opcao == 3 :
        break

    #condição para o não atendimento a todas as condicionais anteriores
    else:
        print("\nOperação inválida, por favor selecionar novamente a operação desejada.\n=> ")






