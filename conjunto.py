#estrutura de dados - lista, tupla, dicionario, tupla

#conjuntos (set)
# estrutura de dados que implementam operações de união, intersecção e diferença
# não admite repetição de elementos
# não mantém a ordem dos elementos, igual dicionario

#conjunto vazio
a = set()

#adicionar valores
a.add(1)
a.add(2)
a.add(3)
a.add("oi")
print(a)
#{1, 2, 3}

#comando in para ver se está dentro do conjunto
print(10 in a) #retorna true or false

#transforma lista em conjunto
b = [1,2,3,4,5]
c = set(b)
#transforma conjunto em lista
d = list(c)
print(c)

#pov se tem uma lista com elemento duplicado e quiser tirar, transforma em conjunto

#operações de diferença um conjunto - outro conjunto
e = set([1,2,3])
f = set([1,2,3])

print(e)
print(f)
print(e - f) #tudo q ta no primeiro e nao ta no segundo
print(e | f) #união, junta tudo
print(e & f) #ta em a e b ao mesmo tempo

#exercicios
l1 = [1,2,3,4,5]
l2 = [4,5,6]

l11 = set(l1)
l22 = set(l2)

#valor comum nas duas
print(l11 & l22)

#valores que só tem na primeira
print(l11 - l22)

#valores que existem apenas na segunda
print(l22 - l11)

#uma lista com valores nao repetidos
print((l11 | l22) - (l11 & l22))
#pode fazer assim tbm: print(l11 ^ l22)

#outro arquivo - exercicio da api de endereço
#importar o dado json da api de viacep para ser um dicionario

#biblioteca requests
import requests

url = "https://viacep.com.br/ws/01001000/json/" #coloca o site que quer bater com a api

txt = requests.get(url)
a = txt.json() #se fizer isso já vai como dicionario
print(a) #ou print(txt.json())

#já pode tratar como dicionario
print(a["cep"])

#tem que o exemplo colocar tudo dentro da função
def extrair_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    txt = requests.get(url)
    a = txt.json()  # se fizer isso já vai como dicionario

    return a

print(extrair_cep("01544050"))

#exericico pokemon
import requests
def pokemon(nome):
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    txt = requests.get(url)
    a = txt.json()  # se fizer isso já vai como dicionario

    #se eu quero mais de uma coisa no return eu coloco ,
    return a["types"][0]["type"]["name"], a["id"]

print(pokemon("ditto"))


#exercicio medalhas - não deu para pegar direto do site pois não estavav funcionando
# (criou-se um arquivo com um dicionario e seus respectivos dados))
# link: https://apis.codante.io/olympic-games/countries
pais = input("Digite o país desejado: ")
for i in range(len(a["data"])):
    if a["data"][i]["name"] == pais:
        print(a["data"][i]["gold_medals"], a["data"][i]["silver_medals"], a["data"][i]["bronze_medals"], a["data"][i]["total_medals"])


#faça uma função para extrair a quantidade de medalhas totais, ouro, prata e bronze do país escolhido

def medalhas(pais):
    for i in range(len(a["data"])):
        if a["data"][i]["name"] == pais:
            nome = a["data"][i]["name"]
            ouro = a["data"][i]["gold_medals"]
            prata = a["data"][i]["silver_medals"]
            bronze = a["data"][i]["bronze_medals"]
            total = a["data"][i]["total_medals"]
            return nome, ouro, prata, bronze, total
print(medalhas("Brasil"))

#ex: gere vários perfis com nome, email, telefone, cidade, estados, país

#no cp, não iremos conseguir pegar dados json, por isso fazer na mesma lógica do ex das medalhas, dentro do pycharm
