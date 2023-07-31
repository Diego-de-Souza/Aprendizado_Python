################### classes set (conjuntos) ###################
#{}.union - serve para unir dois conjuntos
conjunto_a = {1,2}
conjunto_b = {3,4}
conjunto_c = conjunto_a.union(conjunto_b)
print(conjunto_c)

#{}.intersection - faz a iteração dos valores iguais em dois conjuntos
conjunto_d = {1,2,3}
conjunto_e = {2,3,4}
conjunto_f = conjunto_d.intersection(conjunto_e)
print(conjunto_f)

#{}.difference - faz a iteração de valores diferentes em dois conjuntos
conjunto_g = conjunto_d.difference(conjunto_e)
conjunto_h = conjunto_e.difference(conjunto_d)
print(conjunto_g)
print(conjunto_h)

#{}.symmetric_difference - junta todos os elementos em diferentes nos dois conjuntos
conjunto_j = conjunto_d.symmetric_difference(conjunto_e)
print(conjunto_j)

#{}.issubset - verifica se todos os elementos de um conjunto estão em outro conjunto de retorna um valor verdadeiro ou falso
conjunto_i = {1,2,3}
conjunto_m = {4,1,2,5,6,3}
print(conjunto_i.issubset(conjunto_m))
print(conjunto_m.issubset(conjunto_i))

#{}.issuperset - é ao contrário do issubset, verifica ao contrário, ele vê se o que está depois do comando está dentro do outro conjunto
print(conjunto_i.issuperset(conjunto_m))
print(conjunto_m.issuperset(conjunto_i))

#{}.isdisjoint - ele verifica se os valores dos conjuntos são todos diferentes
conjunto_n = {7,8,9}
print(conjunto_e.isdisjoint(conjunto_n))
print(conjunto_e.isdisjoint(conjunto_d))

#{}.add - adiciona um elemento ao conjunto
conjunto_n.add(10)
conjunto_n.add(42)
print(conjunto_n)

#{}.clear - vai limpar todos os valores do seu conjunto
print(conjunto_a)
conjunto_a.clear()
print(conjunto_a)

#{}.copy - vai copiar os valores do seu conjunto
conjunto_b.copy()

#{}.discard - discarta um valor do seu conjunto conforme desejado
conjunto_n.discard(10)
print(conjunto_n)

#{}.pop - vai remover um valor da lista sendo da esquerda para direita
print(conjunto_e)
conjunto_e.pop()
print(conjunto_e)

#{}.remove - remove um elemento do seu conjunto, diferente do discard se vc pedir para remover um elemento que não existe ele vai gerar um erro.
print(conjunto_m)
conjunto_m.remove(2)
print(conjunto_m)

#{}.len - ele verifica a quantidade de elementos ou valores dentro do conjunto
print(len(conjunto_m))

#{}.in - verifica se um valor está dentro de um conjunto
print(1 in conjunto_m)
print(10 in conjunto_m)