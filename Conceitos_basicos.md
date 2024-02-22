# Conceitos Básicos

## Variáveis

Em Linguagens de programação podemos definir valores que podem definir valores que podem sofrer alterações no decorrer da execução do programa. Esse valores recebem o nome de variáveis, pois eles nascem com uma valor e não necessariamente deve permanecer com oo durante a execução do programa.

### Nomes de variáveis

Em Python as variáveis devem iniciar de forma obrigatória com uma letra, porém ela pode conter números e o símbolo underline ( _ ).
Exemplo:

| Nome | Válido | Comentário |
| --- | --- | --- |
| a1 | Sim | Embora contenha número, o nome a1 inicia com uma letra |
| velocidade | Sim | Nome formado por letras |
| velocidade90 | Sim | Formado por letras e números, mas iniciado por uma letra |
| salário_médio | Sim | O underline é permitido e facilita a leitura de nomes grandes |
| salário médio | Não | As variáveis não podem conter espaços em branco |
| _v | Sim | Um declaração desse modo é aceita, mas não usual |
| 1a | Não | Uma variável não pode começar com um número |

### Variáveis numéricas

As variáveis numéricas são aquelas que armazenam números inteiros e de ponto flutuante, os números inteiros são aqueles sem a parte decimal como 1,0,-1, -47, 10000 já os de ponto flutuante são aqueles que tem os decimais como 1.0, 4343.232, 3.14 -1.1.
Python segue assim como outras linguagem como separador nos números o ponto ao invés de virgula como usualmente é feito aqui, sendo isso uma herança da língua inglesa e por isso existe outro forma alternativa de separar números grandes que é utilizar o underline.

```python
1_000 #Mil
>> Resultado = 1000

```

### Variáveis do tipo Lógico

São variáveis  que armazenam  simples sim e não ou Verdadeiro e Falso. Sendo assim uma variável do tipo Booleano.

```python
resultado = True #Verdadeiro
aprovado = False #Falso

```

### Operadores Relacionais

Eles são usados para realizarmos operações lógicas.

| Operador | Operação | Símbolo Matemático |
| --- | --- | --- |
| == | Igualdade | = |
| > | Maior que | > |
| < | Menor que | < |
| != | Diferente |  |
| >= | Maior ou Igual |  |
| <= | Menor ou Igual |  |

Sendo o resultado dessa comparação entre operadores um valor booleano.

### Operadores Lógicos

São os operadores lógicos para operações booleanas. O python por padrão suporta três operadores básicos: **Not** (não), **And** (e), **or** (ou).

| Operador | Operação |
| --- | --- |
| not | Não |
| and | e |
| or | ou |

### Variáveis String

São as variáveis que armazenam cadeias de caracteres como nomes textos em geral. O que chamamos de cadeia de caracteres é uma sequência de símbolos como letras, números, sinais de pontuação etc.
Exemplo:
João e Maria comem pão
E a sintaxe que ele é usado em Python é: `"Isso é uma string"`
Uma string Python tem uma tamanho associado, sendo assim podemos acessar caractere por caractere utilizando a função `len`, que retorna o número que caracteres da string.

### Métodos úteis das strings

### Maiúscula, minúscula e título

```python
curso = "pYtHon"
print(curso.upper())
>>> PYTHON
print(curso.lower())
>>> python
print(curso.title())
>>> Python

```

### Eliminando o espaço em branco

```python
curso = " Python "
print(curso.strip())
>>> "Python"
print(curso.lstrip())
>>> "Python "
print(curso.rstrip())
>>> " Python"

```

### Junções e Centralização

```python
curso = "Python"
print(curso.center(10, "#"))
>>> "##Python##"
print(".".join(curso))
>>> "P.y.t.h.o.n"

```

### Operações com strings

As variáveis string suportam operações como fatiamento, concatenação e composição.
Por fatiamento podemos entender que é a capacidade de utilizar apenas uma parte da string, ou uma fatia.
A concatenação é nada mais que poder juntar duas ou mais strings  em um string maior.
A composição é muito utilizada em mensagens que enviamos à tela e consiste em utilizar strings como modelos em que podemos inserir outras strings

### Concatenação

Os conteúdos das strings podem ser somados, ou melhor concatenados. Para concatenar duas string utilizamos o operador de adição (+). Assim `"AB" + "C"` é igual a `ABC`. Um uso especial de concatenação é a repetição de uma string várias vezes. Para isso usamos o operador de multiplicação (* ).

### Composição/Interpolação

Em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, a segunda é utilizando o método format e a última é utilizando f strings. A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro, por esse motivo iremos focar nas 2 últimas.

### Old Style %

```python
nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e
estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

>>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como
Progamador e utilizo e estou matriculado no curso de Python.

```

### Método Format

```python
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e
estou matriculado no curso de {}.".format(nome, idade, profissao,
linguagem))
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e
estou matriculado no curso de {0}.".format(linguagem, profissao, idade,
nome))

```

### F-string

```python
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho
como {profissao} e estou matriculado no curso de {linguagem}.")
>>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como
Progamador e utilizo e estou matriculado no curso de Python.

```

### Formatar Strings com f-string

```python
PI = 3.14159
print(f"Valor de PI: {PI:.2f}")
>>> "Valor de PI: 3.14"
print(f"Valor de PI: {PI:10.2f}")
>>> "Valor de PI: 3.14"

```

### Fatiamento

Fatiamento de strings é uma técnica utilizada para retornar substrings (partes da string original), informando inicio (start), fim (stop) e passo (step): [start: stop[,step]].

```python
nome = "Guilherme Arthur de Carvalho"
nome[0]
>>> "G"
nome[:9]
>>> "Guilherme"
nome[10:]
>>> "Arthur de Carvalho"
nome[10:16]
>>> "Arthur"
>>>
nome[10:16:2]
>>> "Atu"
>>>
nome[:]

>>> "Guilherme Arthur de Carvalho"
nome[::-1]
>>> "ohlavraC ed ruhtrA emrehliuG"

```

### String de Multiplas linhas

Strings de múltiplas linhas são definidas informando 3 aspas
simples ou duplas durante a atribuição. Elas podem ocupar
várias linhas do código, e todos os espaços em branco são
incluídos na string final.

### Strings Triplas

```python
nome = "Guilherme"
mensagem = f"""
Olá meu nome é {nome}
,
Eu estou aprendendo Python
"""
>>>
Olá meu nome é Guilherme,
Eu estou aprendendo Python

```

## Constantes

Assim como as variáveis, constantes são utilizadas para armazenar valores. Uma constante nasce com uma valor e permanece com ele até o final da execução do programa, ou seja o valor é imutável

### Python não tem constantes?

Não existe uma palavra reservada para informar ao interpretador que o valor é constante. Em algumas linguagem por exemplo: Java e C utilizamos `final` e `const`, respectivamente para declarar uma constante.
Em Python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letras maiúsculas.

## Funções de entrada e saída

### Função Input

A função builtin *input* é utilizada quando queremos ler dados de entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão(tela). A função lê a entrada, converte para string e retorna o valor.
Exemplo:

```python
nome = input("Informe seu nome.:")
>>> Informe seu nome.:

```

### Função Print

A função builtin print é utilizada quando queremos exibir dados na saída padrão. Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais(sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.
Exemplo:

```python
nome = "Evandro"
sobrenome = "Cavalheiro"

print(nome, sobrenome )
print(nome, sobrenome, end="....\\n")
print(nome, sobremome)

```

## Estruturas Condicionais e de Repetição

### Estruturas Condicionais (if, else, elif)

As estruturas condicionais são utilizadas para executar um bloco de código somente se uma condição for verdadeira. Em Python, utilizamos as palavras-chave `if`, `else` e `elif` para construir essas estruturas.

Exemplo de um bloco condicional simples:

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

```

### Estruturas de Repetição (for, while)

As estruturas de repetição permitem executar um bloco de código várias vezes. Em Python, temos as estruturas de repetição `for` e `while`.

Exemplo de um loop `for` que imprime os números de 0 a 9:

```python
for i in range(10):
    print(i)

```

Exemplo de um loop `while` que imprime os números de 0 a 9:

```python
i = 0
while i < 10:
    print(i)
    i += 1

```