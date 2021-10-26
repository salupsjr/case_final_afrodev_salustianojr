from dataframes import Athletes, Coaches, EntriesGender, Medals, Teams
def entrada():
    print("="*40)
    print("OLIMPÍADAS 2021".center(40))
    print("="*40)
    print("""
ESCOLHA A OPÇÃO DESEJADA PARA CONSULTA
[1]  Total de atletas participantes.
[2]  Total de participantes homens.
[3]  Total de participantes mulheres.
[4]  Total de participantes por esporte.
[5]  Total de medalhas por país.
[6]  Ranking por medalhas totais.
[7]  País com mais medalhas de ouro.
[8]  País com mais medalhas de prata.
[9]  País com mais medalhas de bronze.
[10] País com menos medalhas de ouro.
[11] País com menos medalhas de prata.
[12] País com menos medalhas de bronze.
[13] Lista com esportes participantes.
[14] Lista de esportes com mais homens que mulheres.
[15] Lista de esportes com mais mulheres que homens.
[16] Quantidade de treinadores por país.
[17] País com a maior quantidade de treinadores
[18] Quantidade de treinadores por esporte.
[19] Quantos times por esporte cada país tem.""")

def total_de_atletas_participantes():
    # Total de atletas participantes. 1
    print(f"\nO total de atletas participantes nessa olimpíada é de {Athletes.shape[0]} atletas.") # É mostrado mensagem com a quantidades de atletas participantes obtido pelo DataFrame.

def total_participantes_homens():
    # Total de participantes homens. 2
    total_homens = EntriesGender["Male"].sum() # O DataFrame soma as ocorrências da coluna Male e referência para a variável.
    print(f"\nO total de participantes do sexo masculino é de {total_homens} homens.") # Saída que mostra a mensagem com o total de Homens.        
def total_participantes_mulheres():
    # Total de participantes mulheres. 3
    total_mulheres = EntriesGender["Female"].sum() # O DataFrame soma as ocorrências da coluna Female e referência para a variável.
    print(f"\nO total de participantes do sexo feminino é de {total_mulheres} mulheres." ) # Saída que mostra a mensagem com o total de mulheres.
def total_participantes_por_esportes():
    # Total de participantes por esporte. 4
    EntriesGender["Total Participants"] = EntriesGender.Female + EntriesGender.Male # Criação de uma nova coluna no DataFrame que soma as colunas Male e Female.
    tabela_participants = EntriesGender[["Discipline","Total Participants"]] # 
    print(f"\nVeja abaixo a tabela completa com o total de participantes por esporte:\n\n {tabela_participants}")        
def total_medalhas_pais():
    # Total de medalhas por país. 5       
    Medals["Total de Medalhas"] = Medals.Gold + Medals.Silver + Medals.Bronze
    pais = Medals[["Rank","Team/NOC","Total de Medalhas"]]
    print(f"\nVeja abaixo a tabela completa com o total de medalhas por país:\n\n {pais.head(10)}")
def rank_medalhas_totais():
    # Ranking por medalhas totais. 6
    Medals["Total de Medalhas"] = Medals.Gold + Medals.Silver + Medals.Bronze
    Medals.sort_values("Total de Medalhas")
    print(f"\nVeja agora o ranking por total de medalhas:\n\n {Medals.head(10)}")
def mais_ouros():
    # País com mais medalhas de ouro. 7
    rank_ouro = Medals.sort_values("Gold", ascending=False)
    print(rank_ouro.head(10)[["Rank","Team/NOC","Gold"]])
    país = Medals.loc[[Medals[Medals["Gold"] == Medals["Gold"].max()].index[0]],["Team/NOC"]]
    print(f"""\nA maior quantidade de medalhas de ouro é de: {Medals['Gold'].max()} medalhas 
e ela pertence ao(s): \n {país}""")
def mais_prata():
    #País com mais medalhas de Prata. 8
    rank_prata = Medals.sort_values("Silver", ascending=False)
    print(rank_prata.head(1)[["Rank","Team/NOC","Silver"]])
    país = Medals.loc[[Medals[Medals["Silver"] == Medals["Silver"].max()].index[0]],["Team/NOC"]]
    print(f"""\nA maior quantidade de medalhas de prata é de: {Medals['Silver'].max()} medalhas 
e ela pertence ao(s): \n {país}""")
def mais_bronze():
    # País com mais medalhas de Bronze. 9
    rank_bronze = Medals.sort_values("Bronze", ascending=False)
    print(rank_bronze.head(10)[["Rank","Team/NOC","Bronze"]])
    país = Medals.loc[[Medals[Medals["Bronze"] == Medals["Bronze"].max()].index[0]],["Team/NOC"]]
    print(f"""\nA maior quantidade de medalhas de bronze é de: {Medals['Bronze'].max()} medalhas 
e ela pertence ao(s): \n{país}""")
def menos_ouro():
    # País com menos medalhas de ouro. 10
    rank_min_gold = Medals.sort_values("Rank", ascending=False)
    print(rank_min_gold.head(10)[["Rank","Team/NOC","Gold"]])
    país = Medals.loc[[Medals[Medals["Gold"] == Medals["Gold"].min()].index[-1]],["Team/NOC"]]
    print(f"""\nA menor quantidade de medalhas de bronze é de: {Medals['Gold'].min()} medalhas 
e ela pertence ao(s): \n{país}""")
def menos_prata():
    # País com menos medalhas de prata. 11
    rank_min_silver = Medals.sort_values(["Rank"], ascending=False)
    print(rank_min_silver.head(10)[["Rank","Team/NOC","Silver"]])
    país = Medals.loc[[Medals[Medals["Silver"] == Medals["Silver"].min()].index[-1]],["Team/NOC"]]
    print(f"""\nA menor quantidade de medalhas de prata é de: {Medals['Silver'].min()} medalhas 
e ela pertence ao(s): \n {país}""")
def menos_bronze():
    # País com menos medalhas de Bronze. 12
    rank_min_bronze = Medals.sort_values(["Bronze", "Team/NOC"])
    print(rank_min_bronze.head(10)[["Rank","Team/NOC","Bronze"]])
    país = Medals.loc[[Medals[Medals["Bronze"] == Medals["Bronze"].min()].index[-1]],["Team/NOC"]]
    print(f"""\nA menor quantidade de medalhas de bronze é de: {Medals['Bronze'].min()} medalhas 
e ela pertence ao(s): \n {país}""")
def esportes_participantes():
    # Lista com esportes participantes. 13
    modalidades = Teams["Discipline"].unique() 
    print("\nLista com as modalidades participantes nessa Olimpíada de 2021:") 
    for modalidade in modalidades:
        print(modalidade)
def esporte_mais_homens():
    # Lista de esportes com mais homens que mulheres. 14 
    lista_mais_homens = EntriesGender.loc[EntriesGender["Female"] < EntriesGender["Male"]][["Discipline"]]
    print(f"\nLista de modalidades que tem mais homens do que mulheres:\n\n {lista_mais_homens}")
def esporte_mais_mulheres():
    # Lista de esportes com mais mulheres que homens. 15
    lista_mais_mulheres = EntriesGender.loc[EntriesGender["Female"] > EntriesGender["Male"]][["Discipline"]]
    print(f"\nLista de modalidades que tem mais mulheres do que homens:\n {lista_mais_mulheres}")
def treinadores_pais():
    # Quantidade de treinadores por país. 16
    lista_treinadores = Coaches["NOC"].value_counts()
    print(f"Lista de total de treinadores por país:\n{lista_treinadores}")
def maior_quantidade_treinadores():
    # País com a maior quantidade de treinadores 17
    nome_pais = Coaches["NOC"].value_counts().index[0]
    total_tecnicos = Coaches["NOC"].value_counts()[0]
    troca_tradução = nome_pais.replace('Japan', 'Japão')
    print(f"\nO país com maior número de técnicos é o {troca_tradução} com {total_tecnicos} técnicos.")
def treinadores_esportes():
    # Quantidade de treinadores por esporte. 18
    tecnico = Coaches["Discipline"]
    print(f"\nLista de treinadores por esporte:\n{tecnico.value_counts()}")
def times_por_esportes():
    # Quantos times por esporte cada país tem. 19
    times = Teams.groupby(by=["NOC", "Discipline"])["Discipline"].count()
    print(f"\n{times.head(10)}")
        