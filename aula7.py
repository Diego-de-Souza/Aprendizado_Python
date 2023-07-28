########### Metodos da classe list ###########
# [].append -  para adicionar ao a lista
lista = []

lista.append(1)
lista.append("Python")
lista.append([40,30,10])

print(lista)


# [].copy -  para copiar uma lista, criando uma nova
l2 = lista.copy()

print(l2)


# [].count -  para contar quantas vezes determinado objeto tem dentro da lista
cores = ["vermelho","azul","verde","azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))


# [].extend -  para inserir dados em uma lista, como por exemplo uma outra lista
linguagens= ["python","js","c"]
print(linguagens)
linguagens.extend(["java","Csharp"])
print(linguagens)


# [].index -  para mostrar onde é a primeira ocorrencia de determinado objeto dentro da lista
print(linguagens.index("java"))
print(linguagens.index("python"))


# [].pop -  para apaga o ultimo elemento da lista
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))


# [].remove -  para apaga o elemento da lista especificado
linguagens.extend(["python","java","csharp","c"])
print(linguagens)
linguagens.remove("c")
print(linguagens)


# [].reverse -  para espelhar os elementos da lista
linguagens.reverse()
print(linguagens)


# [].sort -  para ordenar os elementos da lista
linguagens.sort()
print(linguagens)

linguagens.sort(reverse=True)
print(linguagens)

linguagens.sort(key=lambda x: len(x))
print(linguagens)
#ou
sorted(linguagens,key=lambda x: len(x))

linguagens.sort(key= lambda x: len(x), reverse=True)
print(linguagens)
#ou
sorted(linguagens,key= lambda x: len(x), reverse=True)


# [].len -  para tamanho da lista, quantidade de elementos
