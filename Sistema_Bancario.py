# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:52:56 2023

@author: bruno
"""


menu = '''

###### Menu inicial ######
Selecione a opção desejada

[d] depositar
[s] sacar
[e] extrato
[q] sair


=>'''

saldo = 0
LIMITE = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
historico = []
n_movimentacao=0


while True:
    opcao = input(menu)
        
    if opcao == 'd':
        print("####### Depósito ##########")
        valor_deposito=int(input("Qual o valor de depósito? \n  =>R$"))
        print ("Por favor, insira as células na máquina \n ...")
        saldo += valor_deposito
        print ("Estaremos realizando a contagem das células. Seu novo saldo pode ser consultado no menu inicial. \n .........................................................") 
        historico.append(valor_deposito)
        
        

        
        
    elif opcao == 's':
        print("####### Saque #######")
        
        if numero_saques > LIMITE_SAQUES:
            print("Não foi possível completar a operação. Número máximo de saques atingido.")
            continue
        else:
            valor_saque=int(input("Qual o valor de saque? \n  =>R$"))
            if valor_saque > saldo:
                print("Não foi possível completar a operação. Saldo insuficiente.")
                continue
            elif valor_saque > LIMITE:
                print("Não foi possível completar a operação. Limite máximo de R$500,00 por saque.")
                continue
            else:
                print ("Por favor, retire as células da máquina \n ...")
                saldo -= valor_saque
                numero_saques += 1
                historico.append(-valor_saque)
                
       
        
        
        
    elif opcao == 'e':
        print("####### Extrato #######")
    
        if saldo == 0 and historico == False:
            print ("Não foram realizadas movimentações")
            continue
        else:
            for n_movimentacao in range(len(historico)):
                movimentacao=  "Saque de       " if historico[n_movimentacao]<0 else "Depósito de     "
                print (f"{movimentacao} R${historico[n_movimentacao]:.2f}")
            print (".............................")
            print (f"Seu Saldo atual é de => R${saldo:.2f}")
            
        
        
            
    elif opcao == 'q':
        break
        
    else:
        print("Operação inválida, por favor selecione a opção desejada novamente")
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
