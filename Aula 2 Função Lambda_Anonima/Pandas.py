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
    "C:/Users/darks/OneDrive/Documents/Repositório/Mineracao_Dados/Aula 2 Função Lambda_Anonima/dados2.csv"
)
print(dado2)

dado = pd.read_excel(
    "C:/Users/darks/OneDrive/Documents/Repositório/Mineracao_Dados/Aula 2 Função Lambda_Anonima/dados.xlsx"
)
print(dado)
