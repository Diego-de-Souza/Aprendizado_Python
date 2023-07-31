#################### Conjuntos ####################
#Tem valores unicos ele elimina valores duplicados, é usado o comando "set"
#obs.:ele não obedece uma ordem, pode apresentar o resultado desordenado
print(set([1,2,3,1,3,4]))
print(set("abacaxi"))
print(set(("palio","gol","celta","palio")))

#outra sintaxe
linguagens = {"python","csharp","python"}
print(linguagens)


############# acessando conjuntos #############
#para consumir os valores de um conjunto deve transformar em uma lista ou utilizando o for enumerate
numeros = {1,2,3,1,4,5,3,6}
numeros1 = list(numeros)
print(numeros1[2])

for num in numeros:
    print(num)

for indice, num2 in enumerate(numeros):
    print(f"{indice}:{num2}")



