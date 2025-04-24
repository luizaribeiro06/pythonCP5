#ordenação
#bubble sort - ordenar o sistea pelo método de bolhas (bolha de maior tamanho sobe mais rapido para o topo da piscina,
#traduzindo para python: maior elemento "borbulha" para ao fim da lista, será o último)

# quando precisa ordenar (de forma crescente, por ex)
# exemplo - números inteiros
# aplicações diretas: rankings, definição de preferencia em atendimentos por prioridade
# aplicações indiretas: otimização de sistemas de busca, manutenção de estruturas de banco de dados
#cair no cp lista, dicionario, api, ordenacao

l = [12,38,25,31,26]
i=2

#trocar os elementos para deixar a lista ordenada
for iteracao in range(len(l)-1,0,-1): #vai andar -1 unidade até chegar no índice 0
    for i in range(iteracao): #len(l) - 1) vai até o fim da lista - 1, depois via -2 e assim vai
        if l[i] > l[i + 1]:
            aux = l[i]
            l[i] = l[i + 1]
            l[i + 1] = aux
        print(l) #mostra a comparação da lista antiga com aatual ordenada
    print()
print(l)


#em função
def bubble_sort(lista):
    n = len(lista)  # tamanho da lista
    for i in range(n):  # repete o processo n vezes
        for j in range(0, n - 1 - i):  # percorre até o último elemento ainda não ordenado, começa no 0, termina na len(lista) e subtrai um pois é o último elemento que precisa
            if lista[j] > lista[j + 1]:  # se o da esquerda for maior que o da direita...
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # ... troca os dois de lugar
    return lista


#selection sort - vai achando o menor elemento e colocando no início da lista

# Exercício: Crie uma função que retorna o índice do menor elemento de uma lista (além disso, declarei o menor elemento por si só)
l= [12,1,95,9,4,25,71]

menor = l[0]
indice= 0
for i in range(1, len(l)):
    if l[i] < menor:
        menor = l[i]
        indice = i
print(menor)
print(indice)

#em função
def indice_menor_elemento(lista):
    menor = lista[0]    # considera o primeiro como menor
    indice = 0          # guarda o índice do menor

    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]  # atualiza o menor valor
            indice_menor = i  # atualiza o índice do menor

    return indice_menor


# Exercício 2: Agora pegue o menor a partir de uma posição inicial dada i, ele tem que retornar o indice desse tal menor de acordo
# com a lista inteira

#como eu estava fazendo
partida =1
indice= 0
menor = l[partida] 
for i in range(partida, len(l)): 
    if l[i] < menor:
        menor = l[i]
        indice = i
print(menor)
print(indice)

#como o professor fez
inicio = 2
indice = inicio
for i in range(inicio+1, len(l)):
    if l[i] < l[indice]:
        indice = i

print(indice)

#transformando em função
def i_menor(l, indice):
    for i in range(indice + 1, len(l)):
        if l[i] < l[indice]:
            indice = i
    return indice

#transformando em for
for i in range(len(l)):
    aux_i = i_menor(l, i)  # menor elemento da lista no começo qyuando ela estava sem rodem
    aux = l[i] #coloca o elemento menor para a auxiliar
    l[i] = l[aux_i]  # vai assumir ser o menor elemento na primeira posição da lista
    l[aux_i] = aux
print(l)

#insertion
#lista ordenada e o último elemento está sem ordem e precisa inserir o elemento na posição correta
#assume que a lista está ordenada entre as posições 0 e 0

#depois que comparar, o valor maior precisa ir indo para frente
l= [12,41,68,71,95,52]
#vai comparando e joga o numero maior para frente
i = 5
for i in range(len(l)): 
    aux = l[i] #elemento atual (a ser inserido no lugar certo)
    j = i - 1 #indice anterior ao atual
    while j >= 0 and l[j] > aux: #se o da esquerda for MAIOR que o atual
        l[j+1] = l[j] #joga uma casa para frente
        j = j - 1 #anda para trás para continuar comparando
        print(l) #mostra a lista a cada troca
    l[j + 1] = aux #insere o valor na posição correta
    print(l)
print(l)

# EX: Altere os algoritmos vistos nesta aula para que estes ordenem uma lista de inteiros em ordem decrescente ao invés de ordem crescente.
#ordem crescente é só alterar o sinal de < para >
#se o exercício fosse "atendimento por prioridade" seria essa a resposta]

def bubble_sort_decrescente(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if lista[j] < lista[j + 1]:  # Troca se o atual for MENOR que o próximo
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def selection_sort_decrescente(lista):
    n = len(lista)
    for i in range(n):
        max_indice = i
        for j in range(i + 1, n):
            if lista[j] > lista[max_indice]:  # Procura o MAIOR valor
                max_indice = j
        lista[i], lista[max_indice] = lista[max_indice], lista[i]
    return lista

def insertion_sort_decrescente(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        # Move os elementos menores que a chave para a direita
        while j >= 0 and lista[j] < chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

#busca sequencial
#pode ser qualquer lista
#percorre cada elemento

#crie uma função que recebe lista, a chave de busca e retorne -1 se nao tiver na lista ou o indice do elemento
def busca(lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            return i  # retorna o índice onde encontrou a chave
    return -1  # se não encontrou

valores = [10, 20, 33, 41, 55]
print(busca(valores, 33)) #saída: 2 (mostra o índice que o elemento está)
print(busca(valores, 99)) #saída -1 pois não encontrou (não está na lista)

#busca binária
#a lista precisa estar ordenada
#divide a lista em metades, por isso tratamos do meio - meio

#crie uma função que recebe lista, a chave de busca e retorne -1 se nao tiver na lista ou o indice do elemento (mesmo exercicio da sequencial)
def busca_binaria(lista, chave):
    #define os limites da lista
    inicio = 0 
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2 #calcula o índice do elemento do meio da parte que estamos procurando

        if lista[meio] == chave: #retorna onde a chave está
            return meio
        elif lista[meio] < chave: #se tiver antes, anda um
            inicio = meio + 1
        else:
            fim = meio - 1 #se tiver depois, volta um

    return -1 #a chave não foi encontrada

#procurando uma palavra no dicionario

#sequencial
def busca_sequencial_palavra(dicionario, palavra):
    indices = [-1] * len(dicionario)  #inicializa a lista de índices com -1 (tamanho da lista)
    count = 0  #contador para controlar os índices encontrados

    for i in range(len(dicionario)):
        chave = dicionario[i][0]  #palavra da tupla
        if chave == palavra:
            indices[count] = i  #amazena o índice encontrado
            count += 1  #incrementa o contador

    #retorna a lista de índices válidos (não negativos), cortada até o número de ocorrências encontradas
    return [indices[i] for i in range(count)]


#binaria
def busca_binaria_palavra(dicionario, palavra):
    inicio = 0
    fim = len(dicionario) - 1
    indices = [-1] * len(dicionario)  #inicializa a lista de índices com -1 (tamanho da lista)
    count = 0  #contador para controlar os índices encontrados

    while inicio <= fim:
        meio = (inicio + fim) // 2
        chave = dicionario[meio][0]  #a palavra que está no meio da lista de tuplas

        if chave == palavra:
            #palavra encontrada, agora buscamos para a esquerda e para a direita
            #para a esquerda
            i = meio
            while i >= 0 and dicionario[i][0] == palavra:
                indices[count] = i
                count += 1
                i -= 1

            #para a direita
            i = meio + 1
            while i < len(dicionario) and dicionario[i][0] == palavra:
                indices[count] = i
                count += 1
                i += 1

            break  #já encontrou todas as ocorrências, podemos sair do loop

        elif chave < palavra:
            inicio = meio + 1
        else:
            fim = meio - 1

    #retorna a lista com os índices encontrados, cortada até o número de ocorrências encontradas
    return sorted(indices[:count])  #ordena a lista e retorna os índices válidos encontrados


'''Crie um sistema que permita o registro de nomes.
Implemente uma função de busca nesse sistema, de forma
sequencial e binária.'''

def registrar_nomes():
    nomes = []
    while True:
        nome = input("Digite um nome para registrar (ou 'fim' para encerrar): ")
        if nome == 'fim':
            break
        nomes.append(nome) 
    return nomes

#função de busca sequencial
def busca_sequencial(nomes, chave):
    indices = []
    for i in range(len(nomes)):
        if nomes[i] == chave:
            indices.append(i)  #adiciona o índice na lista de resultados
    return indices

#função de busca binária (só se a lista estiver ordenada)
def busca_binaria(nomes, chave):
    inicio = 0
    fim = len(nomes) - 1
    indices = []

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if nomes[meio] == chave:
            indices.append(meio)  #encontrou, adiciona o índice
            
            #verificar se há ocorrências à esquerda
            i = meio - 1
            while i >= 0 and nomes[i] == chave:
                indices.append(i)
                i -= 1
            
            #verificar se há ocorrências à direita
            i = meio + 1
            while i < len(nomes) and nomes[i] == chave:
                indices.append(i)
                i += 1

            break
        elif nomes[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1

    return sorted(indices)  #retorna os índices ordenados

# Função principal
def main():
    #registrar nomes
    nomes = registrar_nomes()

    #solicitar nome para busca
    nome_busca = input("Digite o nome a ser buscado: ")

    #busca sequencial
    resultado_sequencial = busca_sequencial(nomes, nome_busca)
    if resultado_sequencial:
        print(f"Nome '{nome_busca}' encontrado nas posições (sequencial): {resultado_sequencial}")
    else:
        print(f"Nome '{nome_busca}' não encontrado (sequencial).")

    #busca binária (assumindo que a lista está ordenada)
    resultado_binario = busca_binaria(nomes, nome_busca)
    if resultado_binario:
        print(f"Nome '{nome_busca}' encontrado nas posições (binária): {resultado_binario}")
    else:
        print(f"Nome '{nome_busca}' não encontrado (binária).")

#rodar o programa
if __name__ == "__main__":
    main()
