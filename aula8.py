####################### Tupla #######################
# obs.: a tupla é algo imultavel, não se pode mudar os valores após criado até o fim do programa

frutas = ("laranja","pera","uva",)#deve ter a virgula no fim
letras = tuple("python")
numeros = tuple([1,2,3,4])
pais = ("Brasil",)

#o acesso da tupla é igual a lista


#tuplas aninhadas
matriz = (
    (1,"a",2),
    ("b",3,4),
    (6,5,"c"),
)

#quando se necessita que uma matriz imutavel se usa a tupla.

#fatiamento com tupla
lista3 = tuple("python")
print(lista3[2:])
print(lista3[:2])
print(lista3[1:3])
print(lista3[0:3:2])
print(lista3[::])
print(lista3[::-1])


#metodos da tupla
#count()
#index()
#len()