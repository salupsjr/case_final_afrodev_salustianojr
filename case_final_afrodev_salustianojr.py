# -*- coding: utf-8 -*-
# Importação dos módulos
from conteudo import (entrada, total_de_atletas_participantes,total_participantes_homens, 
                      total_participantes_mulheres, total_participantes_mulheres, 
                      total_participantes_por_esportes, total_medalhas_pais,
                      rank_medalhas_totais, mais_ouros, mais_prata, mais_bronze, menos_ouro,
                      menos_prata, menos_bronze, esportes_participantes, esporte_mais_homens,
                      esporte_mais_mulheres, treinadores_pais, maior_quantidade_treinadores, 
                      treinadores_esportes, times_por_esportes)

escolha = "S" # Variável escolha já se inicia com [S](Sim) para o teste do while.

while escolha in "sS": # Enquanto S(Sim) ou s for o conteúdo de escolha.
    
    entrada() # É chamado o método entrada() que mostra as opções a serem escolhidas. 
    
    
    opção = int(input("ESCOLHA UMA DAS OPÇÕES ACIMA: ")) # Variável para receber opção escolhida.
    
    
    if opção == 1: # Se opção escolhida for igual a 1... 
        total_de_atletas_participantes() # É chamada do método para tratameto do processo.
    elif opção == 2: # Se opção escolhida for igual a 2... 
        total_participantes_homens()
    elif opção == 3: # Se opção escolhida for igual a 3... 
        total_participantes_mulheres()
    elif opção == 4: # Se opção escolhida for igual a 4... 
        total_participantes_por_esportes()
    elif opção == 5: # Se opção escolhida for igual a 5... 
        total_medalhas_pais()
    elif opção == 6: # Se opção escolhida for igual a 6... 
        rank_medalhas_totais()
    elif opção == 7: # Se opção escolhida for igual a 7... 
        mais_ouros()
    elif opção == 8: # Se opção escolhida for igual a 8... 
        mais_prata()
    elif opção == 9: # Se opção escolhida for igual a 9... 
        mais_bronze()
    elif opção == 10: # Se opção escolhida for igual a 10... 
        menos_ouro()
    elif opção == 11: # Se opção escolhida for igual a 11... 
        menos_prata()
    elif opção == 12: # Se opção escolhida for igual a 12... 
        menos_bronze()
    elif opção == 13: # Se opção escolhida for igual a 13... 
        esportes_participantes()
    elif opção == 14: # Se opção escolhida for igual a 14...        
        esporte_mais_homens()
    elif opção == 15: # Se opção escolhida for igual a 15...        
        esporte_mais_mulheres()
    elif opção == 16: # Se opção escolhida for igual a 16... 
        treinadores_pais()
    elif opção == 17: # Se opção escolhida for igual a 17... 
        maior_quantidade_treinadores()
    elif opção == 18: # Se opção escolhida for igual a 18... 
        treinadores_esportes()
    elif opção == 19: # Se opção escolhida for igual a 19... 
        times_por_esportes()
    else: # Caso a opção escolhida não seja de 1 a 19 mostra a mensagem. 
        print("\nESTÁ OPÇÃO NÃO ESTÁ DISPONÍVEL.")
        
    escolha = input("\nDeseja continuar? [S/N]: ").strip()[0] # Pergunta se usuário deseja continuar consulta.
    
print("\nFINALIZADO COM SUCESSO.")
    