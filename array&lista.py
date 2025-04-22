#array - índice []

a = [1,2,3,4,5]
#print(a[2])

array = [10,20,30,40,50]
array[1] = 25
#print(array)


#listas

#loop para aparecer todos elementos da lista
cidades = ["SP", "RJ", "BH"]
for i in cidades:
    print(i)

#somar todos os números da lista
soma = [1,2,3,4,5]
somas = 0
for i in soma:
    somas += i
print(somas)

#adicionar um elemento (sempre no fim)
lista = [1,2,3]
lista.append(4)

#remover um elemento (pode escolher o índice)
lista.pop(0)

#juntar duas listas
lista1 = [1,2,3]
lista2=[4,5,6]

lista1.extend(lista2) #vai adicionar os elementos da lista 2 na lista 1

#lambda (função simplificada, não pode ter condição e não tem retorn
mult = lambda x: x*x
print(mult(2))

#reverter a string
revert = lambda str: str[::-1]

#verificar se é palindromo
palin= lambda texto: texto == texto[::-1]
print(palin("arara")) #ele aparece como True or False

#como contar vogais em uma string?
def vogais(palavra):
    i = 0
    soma =0
    while i < len(palavra):
        if palavra[i] ==  'a' or palavra[i] ==  'e' or palavra[i] ==  'i' or palavra[i] ==  'o' or palavra[i] ==  'u':
            soma +=1
        i +=1
    return soma

#ouuuuuu usando for >>>>>>
def vogais(palavra):
    qtd = 0
    for i in palavra:
        if palavra[i] ==  'a' or palavra[i] ==  'e' or palavra[i] ==  'i' or palavra[i] ==  'o' or palavra[i] ==  'u':
            qtd +=1
        return qtd

#list comprehension
# estrutura: expression for item in objeto iteravel if condition == True

#exercicios
#quadrados dos números de 1 a 10
lista=[1,2,3,4,5,6,7,8,9,10]
quadrados=[i*i for i in lista]
print(quadrados)

#uma lista contendo apenas os números pares de 1 a 20
pares = [i for i in range(1,21) if i%2 == 0]
print(pares)

#lista contendo o comprimento de cada palavra
palavras = ["Python", "List", "Comprehension", "Exercícios"]
len = [len(i) for i in palavras]
print(len)

#converter a temperatura de celsius --> fahrenreit
temp = [0,10,20,30,40]
f = [i*9/5 + 32 for i in temp]
print(f)

#lista com os números de 1 a 20, substituindo os múltiplos de 3 por "Fizz"
nums=["Fizz" if i%3==0 else i for i in range(1,21)]
print(nums)

#criar uma nova lista apenas com as palavras +5 letras
frutas=["maçã", "banana", "uva", "morango", "abacaxi"]
#cinco = [i for i in frutas if len(i)>5]

#lista representando as coordenadas [x,y] para um grid 3x3
coord = [[x,y] for x in range (3) for y in range (3)]
print(coord)

#forma compactada/alternativa de inicializar uma matriz
l= int(input("Número de linhas: "))
c= int(input("Número de linhas: "))
matriz = [[0] for i in range(c) for i in range(l)]

#tupla
#imutável
#sequência de elementos separados por vírgulas, representados ou não, entre ()
#ex: (18, "abril", 9.5, 1)

#mesmo se tiver apenas um elemento deve usar vírgula
#(18,)

#declaração
variavel = (elemento1, elemento2, ...)
variavel = tuple([elemento1, elemento2, ...])

#acessa o índice da mesma forma que uma lista, fatia tbm

#é possível concatenar tuplas
a = (1,2)
b = (3,4)
print(a+b)

#obtendo a posição de um elemento
print(a.index(2))

#desempacotamento
x,y = (10,20)
# x  = 10
# y = 20

#empacotamento - a tupla pode ser criada apenas separando os elementos por vírgula
18,20
#vira (18,20)

#função enumerate gera uma tupla em que o primeiro valor é o índice e o segundo é o elemento da lista sendo enumerada

l = [5,9,13]
for x, e in enumerate(l):
    print(f"[{x} {e}")

''' fica assim: isso pode ser interessante para saber o indice de cada elemento, mas só daria com tupla?
[0 5]
[1 9]
[2 13]
'''

#list comprehension
tuple(x for x in range(n))
tuple([x for x in range(n)])

#criando uma tupla de forma iterativa
n=int(input("Qts numeros serão lidos? "))
tupla = ()

for i in range(n):
    x = int(input("Entre com o numero: "))
    tupla = tupla + (x,)

print(tupla)

#exercicios
'''
Exercício:
1) Crie um maneira para adicionar elementos em uma
tupla
'''
tupla = (1,2,3)
e = 4

nova_tupla = tupla + (e,) #precisa colocar a vírgula quando só tem um elemento para identificar que é uma tupla
print(nova_tupla)

'''
2) Crie um maneira para remover elementos em uma
tupla
'''
tupla = (1, 2, 3, 4, 3)
e_remover = 3

nova_lista = [] # cria uma lista temporária para armazenar os elementos desejados
for i in tupla:
    if i != e_remover:
        nova_lista.append(i)

nova_tupla = tuple(nova_lista) # converte de volta para tupla

print(nova_tupla)

'''
Exercício:
Crie um maneira para adicionar elementos em uma tupla
def adicionar_elemento(tupla, elemento):
lista = list(tupla) # Converter a tupla em uma lista
lista.append(elemento) # Adicionar o novo elemento
return tuple(lista) # Converter de volta para tupla
# Exemplo de uso
minha_tupla = (1, 2, 3)
nova_tupla = adicionar_elemento(minha_tupla, 4)
print(nova_tupla) # Saída: (1, 2, 3, 4)


Exercício:
Crie um maneira para remover elementos em uma tupla 
def remover_elemento(tupla, elemento):
lista = list(tupla) # Converter a tupla em uma lista 
if elemento in lista:
lista.remove(elemento) # Remover o elemento, se presente
return tuple(lista) # Converter de volta para tupla

# Exemplo de uso
minha_tupla = (1, 2, 3, 4)
nova_tupla = remover_elemento(minha_tupla, 3)
print(nova_tupla) # Saída: (1, 2, 4)
'''
