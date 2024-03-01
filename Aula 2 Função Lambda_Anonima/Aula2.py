# Função Comum
def somaquadrado(a, b):
    somaq = a**2 + b**2
    return somaq


# Chamando a função
somaquadrado(3, 2)

# A função Lambda é a forma de resumir uma função
soma2 = lambda a, b: a**2 + b**2

# Chamando a lambda
soma2(3, 2)

x = lambda f: f / 2
x(4)

# Função Map
# Considere uma lista com várias velocidades de km/h
kmh = [40, 50, 60, 70, 80, 90, 100, 120]
# supunhetamos que vamo converter essa lista por milhas por hora
# Poderiamos usar um for para fazer isso
mph = []
for i in kmh:
    mph.append(i / 1.61)
print(mph)

###################
# usando a função MAp
mph2 = list(map(lambda x: x / 1.61, kmh))
print(mph2)

# list comprehension
mph3 = [x / 1.61 for x in kmh]
print(mph3)

caracteres = [i for i in "Mineracao de dados"]
print(caracteres)
