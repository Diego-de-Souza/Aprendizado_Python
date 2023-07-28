############ Listas: Criação e acesso aos dados ###############
lista1 = ["laranja","maça","uva"]
lista2 = []
lista3 = list("python")
lista4 = list(range(10))
lista5 = ["ferrari","F8",4200000,2023,2900,"São Paulo",True]

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)


################# Método para acessar os valores #################
#buscar na lista 1 o primeiro valor e imprimir
print(lista1[0])
#buscar na lista 1 o terceiro elemento e imprimir
print(lista1[2])
#outra formar de buscar o ultimo elemento, ao inverso
print(lista1[-1])


################# Matriz #################
matriz = [
    [1,"a",2],
    ["b",3,4],
    [6,5,"c"]
]

print(matriz[0]) #[1,"a",2]
print(matriz[0][0]) #1
print(matriz[0][-1]) #2
print(matriz[-1][-1]) #"c"


################# Fatiamento #################
print(lista3[2:])
print(lista3[:2])
print(lista3[1:3])
print(lista3[0:3:2])
print(lista3[::])
print(lista3[::-1])


################# Iterar uma lista #################
carros = ["gol", "celta","palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


################# Compressão de listas #################
########### filtro versão 1 ###########
numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)
########### filtro versão 1 ###########
pares2 = [numero for numero in numeros if numero % 2 == 0]
print(pares2)

########### Modificando valores versão 1 ###########
quadrado = []

for numero in numeros:
    quadrado.append(numero**2)

########### Modificando valores versão 2 ###########
quadrado2 = [numero **2 for numero in numeros]
