import numpy as np  # importando o numpy

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # criando um array

print(a)
# ela parece uma lista mas não é

b = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])  # criando um array

print(b)  # Virou uma matrix

b.max()
b.min()
b.sum()

print(b.std())
# o desvio padrão é uma medida que expressa o grau de dispersão de dados, ou seja o desvio padrao
# indica o quanto um conjunto de dados é uniforme.
# Quando mais próximo de 0 for o desvio padrão, mais homogêneio são dados

# CRIANDO UMA MATRIZ SÓ DE ZEROS
c = np.zeros((3, 3))
print(c)

c2 = np.ones((3, 3))
print(c2)

""" Para criar matrizes esparças que muitos zeros
uma matriz que tem a mesma quantidade de linhas e colunas
em que a diagonal tem uns e o restante da matriz tem zeros utilizamos a função eye"""

c3 = np.eye(10)
print(c3)
