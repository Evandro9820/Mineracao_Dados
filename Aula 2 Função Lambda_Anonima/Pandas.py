""" Para que serve o Pandas
Ele é util para trabalhar com dataframe(basicamente linhas e columans)"""

import pandas as pd

# Criando um dicionário
alunos = {
    "Nome": ["João", "Maria", "Pedro"],
    "Idade": [15, 16, 17],
    "Nota": [7.5, 8, 9.5],
}

# Vamos usar esse dicionario para criar um dataframe
dataframe = pd.DataFrame(alunos)

print(dataframe)

""" Quando criamos um, dataframe o pandas cria indices para cada linha do dataframe e com
isso cada linha tem um indice exclusivo"""

# Mostra as primeiras linhas do dataframe
print(dataframe.head())

# Ele pega as colunas numericas e da a informação sobre essas colunas numericas
print(dataframe.describe())

# Filtra as linhas e colunas
print(dataframe.loc[[0]])
print()
print(dataframe.loc[[0, 2]])
print()
print(dataframe.loc[0:2])
print()
print(dataframe.loc[0:2, "Idade"])
print()
print(dataframe.loc[0:2, ["Idade", "Nota"]])
print()
print(dataframe.loc[dataframe["Nome"] == "João"])
print()

""" Importando arquivos """


dado2 = pd.read_csv(
    "C:/Users/darks/OneDrive/Documents/Repositório/Mineracao_Dados/Aula 2 Função Lambda_Anonima/DataSets/dados2.csv"
)
print(dado2)

dado = pd.read_excel(
    "C:/Users/darks/OneDrive/Documents/Repositório/Mineracao_Dados/Aula 2 Função Lambda_Anonima/DataSets/dados.xlsx"
)
print(dado)

novo_dados = pd.read_csv(
    "C:/Users/darks/OneDrive/Documents/Repositório/Mineracao_Dados/Aula 2 Função Lambda_Anonima/DataSets/athlete_events.csv"
)

print(novo_dados.head(7))

print(
    novo_dados.rename(
        columns={
            "Year": "Ano",
            "City": "Cidade",
            "Name": "Nome",
            "Sex": "Sexo",
            "Sport": "Esporte",
            "Event": "Evento",
            "Medal": "Medalha",
            "Age": "Idade",
            "height": "Altura",
        }
    )
)

print(novo_dados["Medal"].value_counts())
print(novo_dados["Event"].value_counts())
print(novo_dados["Sex"].value_counts())
