import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Geramos alguns dados aleatórios
np.random.seed(0)
X = np.random.rand(100, 1) * 100  # Dados de entrada: tamanho da casa
y = np.random.rand(100, 1) * 10000 + 50 * X  # Dados de saída: preço da casa

# Plotamos os dados para visualizar a relação entre eles
plt.scatter(X, y)
plt.xlabel("Tamanho da casa")
plt.ylabel("Preço da casa")
plt.show()

# Agora dividimos os dados em conjunto de treinamento e de teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Criamos um modelo linear de regressão
model = LinearRegression()

# Treinamos o modelo com os dados de treinamento
model.fit(X_train, y_train)

# Usamos o modelo para prever os preços dos dados de teste
y_pred = model.predict(X_test)

# Plotamos os preços reais e os preços previstos para visualizar a qualidade do modelo
plt.scatter(y_test, y_pred)
plt.xlabel("Preços reais")
plt.ylabel("Preços previstos")
plt.show()

# Calculamos a média do quadrado dos erros para avaliar a qualidade do modelo
mse = mean_squared_error(y_test, y_pred)
print(f"Média do quadrado dos erros: {mse:.2f}")
