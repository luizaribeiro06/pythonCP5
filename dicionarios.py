#dicionario {}
#são estruturas para armazenar dados
#não são sequenciais
#representam uma coleção não ordenada de valores onde cada valor é referenciado através de sua chave
#um objeto par chave valor "CHAVE": valor
#chaves e valores podem ser de diferentes tipos de dados (bool, flat, int, etc)

#dicionario vazio
dicionario ={}
dicionario = dict({})

#esse dict com () é opcional
localizacao = dict({
                "Lat": - 22.81,
                "Long": -47.06
              })

#acessar um valor do dicionario
dicionario["chave"] #a chave PRECISA ser entre ""
#ex:
localizacao["Lat"]
print(localizacao["Lat"])

#para validar a chave se ta no dicionario, usa in
print("Cidade" in localizacao) #vai dar false pois não tem essa chave
print("Lat" in localizacao) #vai dar true pois tem essa chave

#para acessar valor usa o comando get --> nomeDicionario.get
print(localizacao.get("Lat"))

#o tamanho é medido por len as well
#ele irá retornar a qtd de par chave-valor que existe
print(len(localizacao))

#criar novo valor
localizacao["novachave"] = novovalor #só irá ter aspas se for string

#atualizar
localizacao["chaveExistente"] = novovalor

#remover valor
localizacao.pop["chave"]

#ou pode usar del
del localizacao["chave"]

#juntar dois
dic_a = {"A":"Oi", "B": "olá"}
dic_b = {"A":"Oi", "B": "tchau"}
dic_a.update(dic_b)
print(dic_a)

#print(dicionario.keys()) - todas as chaves
#print(dicionario.items()) - chave valor
#print(dicionario.values()) - valor

#copiando //igual lista
dic_b = dic_a.copy()

#função zip permite criar um dicionario a partir de duas listas
pessoas = ["Alice", "Beatriz", "Carlos"]
telefones = ["99999-9999", "99999-1111", "99999-5555"]
contatos = dict(zip(pessoas, telefones))
print(contatos) # irá transformar em um dicionario mesmo

#é possível criar um dicionario cujos valores são listas
pessoas = {}
n = int(input("Quantas pessoas? "))
for i in range(n):
    nome: input()
    idade: int(input())
    sexo = input()
    pessoas[nome] = [idade,sexo]
print(pessoas)
#{"Alice": [20, "F"],
# "Beatriz": [18, "F"],
# "Carlos": [19, "M"]}

print(pessoas["Beatriz"][1])
#se printar isso, o resultado será F

#execicios
'''
Exercício: Escreva uma função que receba uma frase como parâmetro e retorne um dicionário, onde cada chave seja um caractere e seu valor seja o número de vezes que o 
caractere aparece na frase lida. Exemplo: “Os ratos” -> {“O”:1,“ “:1, “s”:2, “r”:1, “a”:1,“t”:1,”o”:1}
'''
def caracteres(frase):
    dicionario = {}
    for caracter in frase: #percorre cada caracter da frase
        if caracter in dicionario: #se o caracter já estiver no dicionario, significa que ele ja apareceu antes, logo, aumenta a contagem
            dicionario[caracter] +=1
        else: #se ainda nao apareceu, adiciona
            dicionario[caracter] = 1

    return dicionario

print(caracteres("Tudo bem"))

'''
Exercício: Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Lembre-se que os elementos duplicados não precisam aparecer em posições consecutivas.
Dica: use um dicionário.
'''
def no_duo(lista):
    dicionario = {} #irá armazenar os itens únicos da lista
    for i in lista: #percorre cada elemento da lista original
        dicionario[i] = True #cada elemento é adicionado como uma chave, logo, se o item já tiver, ele não será duplicado pois chaves são únicas
    return list(dicionario.keys())

lista = [1,2,3,4,1,2]
print(no_duo(lista))

'''
Exercício: Escreva uma função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loja. Por exemplo, para os dados:
lista_de_compras = ’biscoito’, ’chocolate’, ’farinha’ 
supermercado = {
’amaciante’:4.99,
’arroz’:10.90,
’biscoito’:1.69,
’cafe’:6.98,
’chocolate’:3.79,
’farinha’:2.99
}
O valor retornado pela função será 8.47.
'''
def compras(lista, dicionario):
    v_total = 0
    for i in lista: #percorre cada item da lista
        if i in dicionario: #verifica se o item está presente no dicionario
            v_total += dicionario[i] #se sim, soma o preço do item ao total
    return v_total

lista = ["bolo", "chocolate", "farinha"]
dicionario = {
        "bolo": 1.20,
        "chocolate":1.10,
        "farinha": 1.00
}
v_total = compras(lista, dicionario)
print(f'o total das compras é: {v_total:.2f}')

'''
Exercício: Sabe-se que uma molécula de RNA mensageiro é utilizada como base para sintetizar proteínas, no processo denominado de tradução. Cada trinca de bases de RNA mensageiro está relacionado com um aminoácido. Combinando vários aminoácidos, temos uma proteína. Com base na tabela (simplificada) de trincas de RNA abaixo, crie uma função que receba uma string
representando uma molécula de RNA mensageiro válida, segundo essa tabela, e retorne a cadeia de aminoácidos que representam a proteína correspondente.

Exemplo: traducao_rnaM(“UUUUUAUCU”) retorna “Phe-Leu-Ser”
Trinca de RNA Nome do Aminoácido
UUU Phe
CUU Leu
UUA Leu
AAG Lisina
UCU Ser
UAU Tyr
CAA Gln
'''
#fazer depois

'''
Exercício: Escreva uma função que converte números inteiros entre 1 e
999 para algarismos romanos. Não converta o número para uma string.
Use os três dicionários abaixo:
UNIDADES = { 0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX" }
DEZENAS = { 0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC" }
CENTENAS = { 0: "", 1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM" }'''

def numero_romano(numero):
    UNIDADES = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
    DEZENAS = {0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
    CENTENAS = {0: "", 1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}

    #dividir o número em centenas, dezenas e unidades
    centenas = numero // 100
    dezenas = (numero % 100) //10 #pega o resto da divisão do numero por 100 e depois divide por 10 p pegar as dezenas, de fato
    unidades = numero % 10 #pega o resto da divisão do numero por 10

    romano = CENTENAS[centenas] + DEZENAS[dezenas] + UNIDADES[unidades]
    return romano

print(numero_romano(99))
