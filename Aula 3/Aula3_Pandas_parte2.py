import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv(
    "C:/Users/darks/OneDrive/Documents/Repositório/Mineracao_Dados/Aula 2 Função Lambda_Anonima/DataSets/athlete_events.csv"
)

""" print(
    dados.rename(
        columns={
            "Year": "Ano",
            "City": "Cidade",
            "Name": "Nome",
            "Sex": "Sexo",
            "Sport": "Esporte",
            "Event": "Evento",
            "Medal": "Medalha",
            "Age": "Idade",
            "Height": "Altura",
        },
        inplace=True,
    )
) """

""" # Histograma
dados["Idade"].hist()
plt.show()

# BoxPlot
dados.boxplot("Idade")
plt.show()

dados.boxplot(column=["Idade", "Altura"], grid=False)
plt.show()
 """

""" # Grafico com Scatter
x = list(range(2, 21))
y = x
plt.scatter(x, y)
plt.show() """

""" x1 = np.arange(0, 1000, 1)
plt.plot(x1, x1**2)
plt.show()

x2 = np.arange(-1000, 0, 1)
plt.plot(x2, x2**2)
plt.show()


x3 = np.arange(-1000, 1001, 1)
plt.plot(x3, x3)
plt.show()

plt.plot(x1, -(x1**2))
plt.show()
 """

# Nos gráficos acima foram feito com váriaveis criadas por nós agora vamos trabalhar com dados reais
# Criando um dataset com os atletas masculinos
masculino = dados.loc[dados["Sex"] == "M"]
altura_masculino = masculino["Height"]
peso_masculino = masculino["Weight"]
plt.scatter(altura_masculino, peso_masculino)
plt.show()

print(dados.head())

# Agora vamos excluir os dados faltantes, pois nem sempre vamos receber um banco de dados com tudo preenchido de forma correta
dados2 = dados.dropna()

print(dados2.head())

# Porem isso não é viavel já que perdemos muitos dados ao excluir essa linhas que estão faltando
# Por isso preenchemos essas linhas com outras coisas
# Usando isso podemos tratar o dados de algumas forma
enulo = dados.isnull()
print(enulo.head())

""" Porém precisamos saber quandos dados faltantes existe no dataset """
faltantes = elnulo = dados.isnull().sum()

# Podemos ver esse dados de forma percentual
porcentagem = (faltantes / len(dados)) * 100
print(porcentagem)

# Vamos substitur os dados faltantes para isso usaremos a função fillna
dados3 = dados.fillna(0)
print(dados3.head())

# Precisamos criar um conjunto de Treinamento
