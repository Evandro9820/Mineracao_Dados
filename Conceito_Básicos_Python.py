print("Olá mundo")

# Foi falado sobre os conceitos básicos então assim como está no notion

# modulos
import math

math.sqrt = 6


# funções
def parabens():
    print("Parabens")


parabens()


def temaletrau():
    frase = input("digite uma frase")
    if "u" in frase:
        print("tem")
    else:
        print("nao tem")


temaletrau()


def somaquadrado(a, b):
    soma = a**2 + b**2
    return soma


somaquadrado(3, 4)

# Lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
print(lista[0])
print(lista[-1])
print(lista[1:5])

## Metodo .append

lista.append(11)
print(lista)

## Metodo.insert
lista.insert(0, 0)
print(lista)

## Metodo.remove

lista.remove(0)
print(lista)

# tuplas

tupla = (1, 2, 3)
print(tupla)

# Dicionários

dicionario = {
    "Curso": "Sistema de Infromação",
    "Disciplina": "Mineração de Dados",
    "Professor": "José Luiz",
    "Nota": "10",
}
print(dicionario)

dicionario.keys()

dicionario.values()
