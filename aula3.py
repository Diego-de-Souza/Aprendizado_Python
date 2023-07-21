###########  OPERADORES ARITMÉTICOS ###########

produto_1=20
produto_2=10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 * produto_2)
print(produto_1 // produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x =(10+5)*4
y=(10/2)+(25*2)-2 ** 2
print(x)
print(y)

############## OPERADORES DE COMPARAÇÃO  ##############

saldo=450
saque=200

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo < saque)
print(saldo <= saque)

##############  OPERADORES DE ATRIBUIÇÃO  ##############
saldo2=500
saldo2 += 200
print(saldo2)
saldo3=500
saldo3 -= 100
print(saldo3)
saldo4=500
saldo4 *= 100
print(saldo4)
saldo5=500
saldo5 /= 100
print(saldo5)
saldo6=500
saldo6 %= 100
print(saldo6)
saldo7=500
saldo7 **= 100
print(saldo7)

##############  OPERADORES LOGICOS  ##############
saldo8=1000
saque2=200
limite=1000
saldo8 >= saldo2 and saque2 <= limite
saldo8 >= saque2 or saque2 <= limite

contatos_emergencia=[]

not 1000 > 1500
not contatos_emergencia
not "saque 1500"
not ""
#obs. assim como os operadores aritméticos a "()" delimita a ordem de precedencia

##############  OPERADORES DE IDENTIDADE  ##############
curso="Curso de Python"
nome_curso=curso
saldo9, limite = 200, 200

curso is nome_curso
curso is not nome_curso
saldo is limite

##############  OPERADORES DE ASSOCIAÇÃO  ##############
frutas= ["laranja","uva","limão"]
saques = [1500, 100]

"Python" in curso
"maça" not in frutas
200 in saques
